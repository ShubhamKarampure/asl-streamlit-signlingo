import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from styles import page_setup,hide_navbar,unhide_nav_bar

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

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

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
