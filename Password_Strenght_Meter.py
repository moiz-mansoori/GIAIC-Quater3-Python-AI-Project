import streamlit as st
import re
import secrets
import string
import math  # Add math import for potential entropy calculation

class PasswordStrengthMeter:
    def __init__(self):
        self.characters = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
            "digits": string.digits,
            "special": "!@#$%^&*"
        }
        self.weak_passwords = {
            "password", "qwerty", "123456", "admin", 
            "mypassword", "welcome", "password123", 
            "abc123", "111111", "iloveyou",'tryagain'
        }

    def check_password_strength(self, password):
        """
        Comprehensive password strength analysis.
        
        Args:
            password (str): Password to analyze
        
        Returns:
            dict: Strength analysis results
        """
        score = 0
        feedback = []

        # Checking weak passwords list
        if password.lower() in self.weak_passwords:
            return {
                "score": 0, 
                "strength": "Very Weak", 
                "color": "red", 
                "feedback": ["❌ Common and easily guessable password"]
            }

        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ At least 8 characters required")

        char_checks = {
            key: bool(re.search(fr"[{chars}]", password)) 
            for key, chars in self.characters.items()
        }
        score += sum(char_checks.values())

        # Feedback for missing any character types
        if not char_checks["upper"]:
            feedback.append("❌ Add an uppercase letter")
        if not char_checks["lower"]:
            feedback.append("❌ Add a lowercase letter")
        if not char_checks["digits"]:
            feedback.append("❌ Add a number")
        if not char_checks["special"]:
            feedback.append("❌ Add a special character (!@#$%^&*)")

        if len(set(password)) < len(password) * 0.7:
            feedback.append("⚠️ Avoid too many repeating characters")
            score = max(0, score - 1)

        # Determine strength levels
        strength_levels = [
            (5, "Strong", "green"), 
            (4, "Moderate", "orange"), 
            (0, "Weak", "red")
        ]
        
        for level, label, color in strength_levels:
            if score >= level:
                return {
                    "score": score, 
                    "strength": label, 
                    "color": color, 
                    "feedback": feedback or ["✅ Good password!"],
                    "entropy": self._calculate_entropy(password)
                }

    def _calculate_entropy(self, password):
        """
        Calculate password entropy.
        
        Args:
            password (str): Password to calculate entropy for
        
        Returns:
            float: Calculated entropy
        """
        # Determine character set size
        char_set_size = 0
        if re.search(r'[a-z]', password):
            char_set_size += 26
        if re.search(r'[A-Z]', password):
            char_set_size += 26
        if re.search(r'\d', password):
            char_set_size += 10
        if re.search(r'[!@#$%^&*]', password):
            char_set_size += 10
        
        # Calculate entropy
        return round(len(password) * math.log2(char_set_size), 2) if char_set_size > 0 else 0

    def generate_strong_password(self, length=12):
        """
        Generate a cryptographically secure password.
        
        Args:
            length (int): Desired password length
        
        Returns:
            str: Generated password
        """
        # Ensure at least one character from each type
        all_chars = "".join(self.characters.values())
        password = [secrets.choice(chars) for chars in self.characters.values()]
        
        password += [secrets.choice(all_chars) for _ in range(length - len(password))]
        
        # For randomness
        secrets.SystemRandom().shuffle(password)
        
        return "".join(password)

def main():
    st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")
    
    # Initialize password meter
    password_meter = PasswordStrengthMeter()

    # Title and description
    st.title("🔐 Password Strength Meter")
    st.markdown("""
    Check your password strength and generate secure alternatives.
    
    **Features:**
    - Password strength analysis
    - Detailed feedback
    - Secure password generation
    """)

    tab1, tab2 = st.tabs(["Check Password", "Generate Password"])

    with tab1:
        st.header("Check Password Strength")
        
        # Password input
        password = st.text_input("Enter your password", type="password")
        
        if password:
            # Analyze password
            result = password_meter.check_password_strength(password)
            
            # Display strength
            st.markdown(f"**Strength:** <span style='color:{result['color']}'>{result['strength']}</span>", 
                        unsafe_allow_html=True)

            st.subheader("Feedback")
            for msg in result['feedback']:
                st.markdown(msg)
            
            # Show entropy if calculated
            if 'entropy' in result:
                st.metric("Password Entropy", result['entropy'])

    with tab2:
        st.header("Generate Strong Password")
        
        length = st.slider("Password Length", 12, 24, 16)
        
        # Generate button
        if st.button("Generate Password"):
            # Create password
            generated_password = password_meter.generate_strong_password(length)
            
            # Display generated password
            st.success("🎲 Generated Password:")
            st.code(generated_password)
            
            # Analyze generated password
            result = password_meter.check_password_strength(generated_password)
            st.markdown(f"**Strength:** <span style='color:{result['color']}'>{result['strength']}</span>", 
                        unsafe_allow_html=True)

    # Security tips
    st.markdown("---")
    st.markdown("💡 **Tips for a Strong Password:**")
    st.markdown("""
    - Use uppercase & lowercase letters
    - Include numbers & special characters
    - Avoid common words or personal details
    - Make it at least 12 characters long
    """)

    st.markdown("### Author: \n **MOIZ MANSOORI**")

if __name__ == "__main__":
    main()