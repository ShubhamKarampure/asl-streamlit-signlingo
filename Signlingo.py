import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from styles import page_setup,hide_navbar,unhide_nav_bar
import json
import sqlite3

conn = sqlite3.connect(
    "signlingo.db"
)

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Profile (
                    username TEXT PRIMARY KEY,
                    name TEXT,
                    email_id TEXT
                )''')

c.execute(
    """CREATE TABLE IF NOT EXISTS Alphabet (
                    username TEXT,
                    letter TEXT,
                    PRIMARY KEY (username, letter),
                    FOREIGN KEY(username) REFERENCES User(username)
                )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS Words (
                    username TEXT,
                    word TEXT,
                    PRIMARY KEY (username, word),
                    FOREIGN KEY(username) REFERENCES User(username)
                )"""
)

conn.commit()

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(hide_navbar(), unsafe_allow_html=True)

def get_username(self):
        if st.session_state['LOGOUT_BUTTON_HIT'] == False:
            fetched_cookies = self.cookies
            if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
                username=fetched_cookies['__streamlit_login_signup_ui_username__']
                return username

def get_name(self):
        with open("_secret_auth_.json","r") as auth:
             user_data = json.load(auth)
             current_user = get_username(self)
             for user in user_data:
                  if user["username"] == current_user:
                    return user["name"]

def get_email(self):
    with open("_secret_auth_.json","r") as auth:
        user_data = json.load(auth)
        current_user = get_username(self)
        for user in user_data:
            if user["username"] == current_user:
                return user["email"]

def add_profile_to_database(current_user):
    try:
        conn = sqlite3.connect("signlingo.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO Profile (username, name, email_id)
                                VALUES (?, ?, ?)""",
                (current_user["username"], current_user["name"], current_user["email"]),
            )
    except Exception as e:
        print(f"Error occurred: {e}")
        # Log the exception or handle it appropriately
    finally:
        if conn:
            conn.close()

login_obj = __login__(
    auth_token="courier_auth_token",
    company_name="signlingo",
    width=200,
    height=250,
    logout_button_name="Logout",
    hide_menu_bool=True,
    hide_footer_bool=True,
    lottie_url="https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json",
)


logged_in = login_obj.build_login_ui()

if logged_in:

    current_user = {
        "username": get_username(login_obj),
        "name": get_name(login_obj),
        "email": get_email(login_obj),
        "id": None,
    }

    if "current_user" not in st.session_state:
        st.session_state["current_user"] = current_user
    else:
        st.session_state["current_user"] = current_user

    add_profile_to_database(current_user)

    st.markdown(unhide_nav_bar(), unsafe_allow_html=True)
    # Display other content
    st.write("# Welcome to Signlingo! 👋")
    # Other content...
    st.markdown(
        """
    <div class="section">
        <a class="link" href="About_Us">About</a> | 
        <a class="link" href="#features">Features</a> | 
        <a class="link" href="#contact">Contact</a>
    </div>

    <div class="section">
        <h2 class="header">Master Sign Language Effortlessly</h2>
        <p>SignLingo is an innovative web application designed for individuals who are mute or communicate primarily through sign language. Similar to popular language learning platforms like DuoLingo, SignLingo aims to provide an interactive and engaging way for users to learn and practice sign language.</p>
    
    </div>

    <div class="section">
        <h2 class="header">About SignLingo</h2>
        <p>SignLingo is revolutionizing the way we learn and practice sign language. Powered by cutting-edge technology, SignLingo utilizes OpenCV for image processing and MediaPipe action detection, ensuring an accurate and seamless learning experience.</p>
    </div>

    <div class="section">
        <h2 class="header">Features</h2>
        <ul>
            <li>Interactive lessons</li>
            <li>Real-time feedback</li>
            <li>Engaging practice sessions</li>
            <li>Progress tracking</li>
        </ul>
    </div>

    <div class="section">
        <h2 class="header">Contact Us</h2>
        <p>Have questions or feedback? We'd love to hear from you!</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
