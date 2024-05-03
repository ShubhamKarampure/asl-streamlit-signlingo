import cv2
import streamlit as st
import time
import random
from model import prediction_model
from components import progress_bar
from styles import page_setup, page_with_webcam_video

if "page" not in st.session_state or st.session_state["page"] != "testpage":
    cv2.destroyAllWindows()
    st.session_state["page"] = "testpage"
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

ALPHABET_LIST = [
    "A",
    "B",
    "C",
    "D",
    "E",
]
NUM_ALPHABETS = len(ALPHABET_LIST)

if "test" not in st.session_state:
    st.session_state["test"] = random.randint(0, NUM_ALPHABETS - 1)

# Element struction
title_placeholder = st.empty()  # stores letter title
col1, col2 = st.columns([0.5, 0.5])
with col1:
    charachter_placeholder = st.empty()  # to display video
    score_placeholder = st.empty()
with col2:
    webcam_placeholder = st.empty()  # to display webcam

matched_bar = st.empty()


# creating the progress bar
prob = 0
score = 0

while True and st.session_state["page"] == "testpage":

    if cap is not None or cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:
        title_placeholder.header(
            "Test your understanding 📝"
        )

        charachter = ALPHABET_LIST[st.session_state["test"]]
        charachter_placeholder.markdown('<div class="letterToFind">{}</div>'.format(charachter), unsafe_allow_html=True)

        frame, prob = prediction_model(frame, st.session_state["test"])
        frame = cv2.resize(
            frame, (500, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC
        )
        webcam_placeholder.image(frame, channels="BGR")

        matched_bar.markdown(
            progress_bar(prob),
            unsafe_allow_html=True,
        )

        score_placeholder.subheader(f"Score {score}")

        if prob == 100:
            st.balloons()
            score += 10
            st.session_state["test"] = random.randint(0, NUM_ALPHABETS - 1)
            time.sleep(2)


cap.release()
cv2.destroyAllWindows()
