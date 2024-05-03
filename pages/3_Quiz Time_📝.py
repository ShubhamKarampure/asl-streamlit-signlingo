import streamlit as st
import random
import time
import streamlit_book as stb
from styles import page_setup,page_with_webcam_video
from urls import video_urls

if "page" not in st.session_state:
    st.session_state["page"] = "test"
st.session_state["page"] = "test"

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

title_placeholder = st.empty()
title_placeholder.header("Quiz Time")

def question():
    col1, col2 = st.columns([0.5,0.5], gap="medium")
    # Function to update video display
    def update_video(charachter):
        return f"""
        <div class="video-wrapper">
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scaleX(-1);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div>  
        """

    with col2:
        video_placeholder = st.empty()

    # Initialize session state
    if "correct_option" not in st.session_state:
        st.session_state["correct_option"] = None

    if "options" not in st.session_state:

        st.session_state["options"] = None
    if st.session_state["correct_option"] is not None:
        video_placeholder.markdown(
            update_video(st.session_state["correct_option"]), unsafe_allow_html=True
        )

    # Check if the correct option is initialized
    if st.session_state["correct_option"] is None:

        st.session_state["correct_option"] = random.choice(list(video_urls.keys()))

        video_placeholder.markdown(
            update_video(st.session_state["correct_option"]), unsafe_allow_html=True
        )

        correct_option = st.session_state["correct_option"]
        remaining_chars = [char for char in video_urls.keys() if char != correct_option]
        incorrect_options = random.sample(remaining_chars, 3)
        if st.session_state["options"] is None:
            options = [correct_option] + incorrect_options
            random.shuffle(options)
            st.session_state["options"] = options 

    with col1:
        st.subheader("Choose the best option:")
        checked_answer, correct_answer = stb.single_choice(
            " ",
            st.session_state["options"],
            st.session_state["options"].index(st.session_state["correct_option"]),
            success=f"Perfect! It's letter {st.session_state['correct_option']}!",
            error="Sadly, that's not true",
            button="Click to check",
        )

    # Check the answer
    if checked_answer:
        if correct_answer:
            st.balloons()
            st.session_state["correct_option"] = None
            st.session_state["options"] = None
            video_placeholder.empty()
            time.sleep(2)
            st.experimental_rerun()


question()
