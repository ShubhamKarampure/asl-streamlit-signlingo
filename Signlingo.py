import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from styles import page_setup,hide_navbar,unhide_nav_bar
import json
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aj19@SQL",
    database="signlingo"
     
     )

    # Create a cursor object
cursor = conn.cursor()

st.set_page_config(
        page_title="signlingo",
)

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(hide_navbar(), unsafe_allow_html=True)

__login__obj = __login__(
    auth_token="courier_auth_token",
    company_name="signlingo",
    width=200,
    height=250,
    logout_button_name="Logout",
    hide_menu_bool=True,
    hide_footer_bool=True,
    lottie_url="https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json",

)


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

             





LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.session_state["current_user"] = {"username" :get_username(__login__obj), "name":get_name(__login__obj),"email":get_email(__login__obj),} 
    # print(st.session_state['current_user'])
    # print(get_name(__login__obj))
    print(get_name(__login__obj))

    print(st.session_state["current_user"])
    global current_user 
    current_user = st.session_state["current_user"]
    try:
        with conn.cursor() as cursor:
             query = f"insert into profile values ('{current_user['username']}', '{current_user['name']}', '{current_user['email']}');"
             cursor.execute(query)
             conn.commit()
             print("New profile identified and updated")
    except Exception as e:
         print(e)
    finally:
        # conn.close()
        pass 
         



    st.markdown(unhide_nav_bar(), unsafe_allow_html=True)

    st.write("# Welcome to Signlingo! 👋")

    if 'page' not in st.session_state:
        st.session_state['page'] = 'homepage'

    st.session_state['page'] = 'homepage'

    import streamlit as st

    # Content
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
