import streamlit as st
import pandas as pd
from datetime import datetime
import hashlib


st.set_page_config(
    page_title="Growth Mindset Tracker",
    page_icon="🌱",
    layout="wide"
)

if 'reflections' not in st.session_state:
    st.session_state.reflections = []
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'users' not in st.session_state:
    st.session_state.users = {}  # Store user data (in a real app, use a secure database)

def hash_password(password):
    """Create a hashed version of the password"""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(email, password):
    """Check if email and password are valid or no"""
    if email in st.session_state.users:
        if st.session_state.users[email] == hash_password(password):
            return True
    return False

def signup(email, password):
    """Register a new user"""
    if email in st.session_state.users:
        return False
    st.session_state.users[email] = hash_password(password)
    return True

def login_page():
    st.title("🌱 Growth Mindset Journey")
    st.subheader("Welcome! Please login or signup to continue")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            
            if submit:
                if authenticate(email, password):
                    st.session_state.authenticated = True
                    st.session_state.current_user = email
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Please sign up first, then login OR Invalid email or password")
    
    with tab2:
        with st.form("signup_form"):
            new_email = st.text_input("Email")
            new_password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submit = st.form_submit_button("Sign Up")
            
            if submit:
                if new_password != confirm_password:
                    st.error("Passwords do not match")
                elif not new_email or not new_password:
                    st.error("Please fill in all fields")
                elif signup(new_email, new_password):
                    st.success("Account created successfully! Please login now.")
                else:
                    st.error("Email already exists")

def main_app():
    st.title(f"🌱 Growth Mindset Journey - Welcome {st.session_state.current_user}")
    
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.current_user = None
        st.rerun()

    with st.sidebar:
        st.header("What is Growth Mindset?")
        st.info("""
        A growth mindset is the belief that your abilities can be developed through 
        dedication, hard work, and learning from feedback. - Carol Dweck
        """)
        
        st.markdown("### Key Principles")
        st.write("• Embrace challenges as opportunities")
        st.write("• Learn from mistakes and feedback")
        st.write("• Put in effort to grow and improve")
        st.write("• Stay persistent through difficulties")

    tab1, tab2, tab3 = st.tabs(["Daily Reflection", "Progress Tracker", "Learning Resources"])

    with tab1:
        st.header("Daily Learning Reflection")
        
        with st.form("reflection_form"):
            date = st.date_input("Date", datetime.now())
            challenge = st.text_area("What challenges did you face today?")
            learning = st.text_area("What did you learn from these challenges?")
            mindset_rating = st.slider(
                "Rate your growth mindset today (1-10):",
                1, 10, 5
            )
            next_steps = st.text_area("What are your next steps for improvement?")
            
            submitted = st.form_submit_button("Save Reflection")
            if submitted:
                reflection = {
                    'user': st.session_state.current_user,
                    'date': date,
                    'challenge': challenge,
                    'learning': learning,
                    'mindset_rating': mindset_rating,
                    'next_steps': next_steps
                }
                st.session_state.reflections.append(reflection)
                st.success("Reflection saved successfully!")

    with tab2:
        st.header("Your Growth Journey")
        if st.session_state.reflections:
            user_reflections = [r for r in st.session_state.reflections 
                              if r['user'] == st.session_state.current_user]
            
            if user_reflections:
                df = pd.DataFrame(user_reflections)
                
                st.subheader("Mindset Rating Trend")
                st.line_chart(df.set_index('date')['mindset_rating'])
                
                # Displaying a reflection history
                st.subheader("Reflection History")
                display_df = df.drop('user', axis=1)  
                st.dataframe(display_df)
            else:
                st.info("Start tracking your growth by adding daily reflections!")
        else:
            st.info("Start tracking your growth by adding daily reflections!")

    with tab3:
        st.header("Growth Mindset Resources")
        
        # Video section (placeholder)
        st.subheader("How to learn Streamlit: Watch this video.")
        st.video("https://youtu.be/8W8NQFFbDcU?si=vyyjeGaT4VM6KO5K")
        
        st.subheader("Recommended Reading")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            * **Mindset: The New Psychology of Success** by Carol Dweck
            * **Grit: The Power of Passion and Perseverance** by Angela Duckworth
            """)
        
        with col2:
            st.markdown("""
            * **Atomic Habits** by James Clear
            * **Peak: Secrets from the New Science of Expertise** by Anders Ericsson
            """)

def main():
    if not st.session_state.authenticated:
        login_page()
    else:
        main_app()

if __name__ == "__main__":
    main()