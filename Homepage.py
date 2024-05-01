import streamlit as st
import cv2

st.set_page_config(
    page_title="signlingo",
)

st.write("# Welcome to Signlingo! 👋")

if 'page' not in st.session_state:
    st.session_state['page'] = 'homepage'

st.session_state['page'] = 'homepage'


import streamlit as st


# Content
st.markdown(
    """
    <div class="section">
        <a class="link" href="#about">About</a> | 
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
