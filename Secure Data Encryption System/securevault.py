import streamlit as st
import hashlib
import json
import os
from cryptography.fernet import Fernet, InvalidToken
from datetime import datetime, timedelta
from typing import Dict, Optional, Any

# Security constants
KEY_FILE = "key.key"
DATA_FILE = "vault.json"
# Pre-computed hash for "admin123" - replace with your own in production
ADMIN_PASSWORD_HASH = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
LOCKOUT_MINUTES = 15
MAX_ATTEMPTS = 3

# Session State Initialization
if "data" not in st.session_state:
    st.session_state.data = {}
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "lock_time" not in st.session_state:
    st.session_state.lock_time = None
if "admin" not in st.session_state:
    st.session_state.admin = False

# Lockout Check
def is_locked() -> bool:
    """Check if the system is currently locked due to failed attempts."""
    if st.session_state.lock_time and datetime.now() < st.session_state.lock_time:
        return True
    # Reset lock if time has passed
    if st.session_state.lock_time and datetime.now() >= st.session_state.lock_time:
        st.session_state.lock_time = None
    return False

# Load or Generate Key
def load_key() -> Fernet:
    """Load existing encryption key or generate a new one."""
    try:
        if not os.path.exists(KEY_FILE):
            with open(KEY_FILE, "wb") as f:
                f.write(Fernet.generate_key())
        with open(KEY_FILE, "rb") as f:
            return Fernet(f.read())
    except Exception as e:
        st.error(f"Error with encryption key: {str(e)}")
        return None

# Load Vault
def load_data() -> None:
    """Load the vault data from file."""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                st.session_state.data = json.load(f)
    except Exception as e:
        st.error(f"Error loading vault: {str(e)}")
        st.session_state.data = {}

# Save Vault
def save_data() -> None:
    """Save the vault data to file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(st.session_state.data, f)
    except Exception as e:
        st.error(f"Error saving vault: {str(e)}")

# Hashing
def hash_passkey(passkey: str) -> str:
    """Create a secure hash of the passkey."""
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt & Decrypt
def encrypt_text(f: Fernet, text: str) -> str:
    """Encrypt plain text using Fernet."""
    try:
        return f.encrypt(text.encode()).decode()
    except Exception as e:
        st.error(f"Encryption error: {str(e)}")
        return ""

def decrypt_text(f: Fernet, enc: str, passkey: str) -> Optional[str]:
    """Decrypt encrypted text using passkey."""
    # Check if locked
    if is_locked():
        return None
        
    # Verify passkey
    hashed = hash_passkey(passkey)
    entry = st.session_state.data.get(enc)
    
    if not entry or entry["passkey"] != hashed:
        st.session_state.attempts += 1
        if st.session_state.attempts >= MAX_ATTEMPTS:
            st.session_state.lock_time = datetime.now() + timedelta(minutes=LOCKOUT_MINUTES)
        return None
    
    # Attempt decryption
    try:
        result = f.decrypt(enc.encode()).decode()
        st.session_state.attempts = 0  # Reset attempts on success
        return result
    except InvalidToken:
        st.session_state.attempts += 1
        if st.session_state.attempts >= MAX_ATTEMPTS:
            st.session_state.lock_time = datetime.now() + timedelta(minutes=LOCKOUT_MINUTES)
        return None
    except Exception as e:
        st.error(f"Decryption error: {str(e)}")
        return None

# UI Sections
def home() -> None:
    """Display home page."""
    st.title("🔐 SecureVault")
    st.write("Store and retrieve data securely with encrypted passkeys.")
    st.markdown("""
    # Secure Encryption:
    ###  Your data is encrypted using strong algorithms.
        This application helps you securely store and retrieve sensitive data using encryption technology.
    """)
    st.info("""
    ### How to use SecureVault:
    1. Go to the **Store** section to encrypt your data
    2. Create a strong passkey to protect your data
    3. Save the encrypted text that is generated
    4. Use the **Retrieve** section to decrypt your data later
    """)

def store(f: Fernet) -> None:
    """Display data storage page."""
    st.subheader("📥 Store Secret")
    
    text = st.text_area("Enter Data to Encrypt", height=150)
    passkey = st.text_input("Create Passkey", type="password")
    confirm = st.text_input("Confirm Passkey", type="password")
    
    if st.button("Encrypt & Save"):
        if not text:
            st.warning("Please enter data to encrypt.")
            return
            
        if not passkey:
            st.warning("Please create a passkey.")
            return
            
        if passkey != confirm:
            st.error("Passkeys do not match!")
            return
            
        # Create encrypted data with timestamp
        enc = encrypt_text(f, text)
        if enc:
            st.session_state.data[enc] = {
                "passkey": hash_passkey(passkey),
                "created": datetime.now().isoformat()
            }
            save_data()
            st.success("✅ Data encrypted and saved successfully!")
            st.code(enc)
            st.info("Keep this encrypted text safe. You'll need it to retrieve your data.")

def retrieve(f: Fernet) -> None:
    """Display data retrieval page."""
    st.subheader("📤 Retrieve Secret")
    
    # Check for lockout first
    if is_locked():
        remaining = st.session_state.lock_time - datetime.now()
        minutes = int(remaining.total_seconds() // 60)
        seconds = int(remaining.total_seconds() % 60)
        st.error(f"🔒 Too many failed attempts. Locked for {minutes}m {seconds}s.")
        st.info("You can use the Admin panel to unlock if necessary.")
        return
    
    enc = st.text_area("Paste Encrypted Text")
    passkey = st.text_input("Enter Passkey", type="password")
    
    if st.button("Decrypt"):
        if not enc or not passkey:
            st.warning("Both encrypted text and passkey are required.")
            return
            
        # Check if the encrypted text exists in our vault
        if enc not in st.session_state.data:
            st.error("Invalid encrypted text. This data doesn't exist in the vault.")
            return
            
        result = decrypt_text(f, enc, passkey)
        if result:
            st.success("✅ Successfully decrypted:")
            st.text_area("Your Secret Data", result, height=150)
        else:
            attempts_left = MAX_ATTEMPTS - st.session_state.attempts
            st.error(f"❌ Incorrect passkey. Attempts left: {attempts_left}")

def admin() -> None:
    """Display admin panel."""
    st.subheader("🔐 Admin Panel")
    
    if not st.session_state.admin:
        pwd = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            if hash_passkey(pwd) == ADMIN_PASSWORD_HASH:
                st.session_state.admin = True
                st.session_state.attempts = 0
                st.session_state.lock_time = None
                st.success("✅ Admin login successful!")
            else:
                st.error("❌ Incorrect admin password!")
    else:
        st.success("Logged in as Admin")
        
        # Display vault statistics
        st.subheader("Vault Statistics")
        st.write(f"Total entries in vault: {len(st.session_state.data)}")
        
        # Unlock account option
        if st.button("🔓 Unlock Account"):
            st.session_state.attempts = 0
            st.session_state.lock_time = None
            st.success("✅ Account unlocked successfully.")
        
        # Reset vault with confirmation
        st.subheader("Danger Zone")
        if st.button("🚨 Reset Vault"):
            confirm = st.text_input("Type 'DELETE' to confirm clearing the vault:").strip()
            if confirm == "DELETE":
                st.session_state.data = {}
                save_data()
                st.success("✅ Vault cleared successfully.")
            elif confirm:
                st.error("Confirmation text doesn't match. Vault not cleared.")
                
        if st.button("Logout"):
            st.session_state.admin = False
            st.success("✅ Logged out successfully.")

# Run App
def main() -> None:
    st.set_page_config(page_title="SecureVault", page_icon="🔐")
    
    cipher = load_key()
    if not cipher:
        st.error("Failed to initialize encryption. Please check file permissions.")
        return
        
    load_data()
    
    # Add a status indicator in the sidebar
    st.sidebar.title("SecureVault")
    if is_locked():
        st.sidebar.warning("🔒 Account locked")
    elif st.session_state.admin:
        st.sidebar.success("✅ Admin logged in")
    
    menu = st.sidebar.radio("Menu", ["Home", "Store", "Retrieve", "Admin"])
    
    if menu == "Home":
        home()
    elif menu == "Store":
        store(cipher)
    elif menu == "Retrieve":
        retrieve(cipher)
    elif menu == "Admin":
        admin()
        
    # Add footer
    st.sidebar.markdown("---")    
    st.sidebar.caption("SecureVault v1.1")

if __name__ == "__main__":
    main()