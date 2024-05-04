import cv2
import streamlit as st
import time
import random
from model import prediction_model
from components import progress_bar, update_video
from styles import page_setup, page_with_webcam_video

if "page" not in st.session_state or st.session_state["page"] != "testpage":
    cv2.destroyAllWindows()
    st.session_state["page"] = "testpage"
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

st.markdown("""
        <style>img {
        border-radius: 1rem;
        height:336px;
        width:336px;
        }</style>""",unsafe_allow_html=True)

ALPHABET_LIST = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "R",
    17: "S",
    18: "T",
    19: "U",
    20: "V",
    21: "W",
    22: "X",
    23: "Y",
}
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

intial_time = time.time()
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

        frame, prob = prediction_model(frame, ALPHABET_LIST[st.session_state["test"]])
        frame = cv2.resize(
            frame, (500, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC
        )
        webcam_placeholder.image(frame, channels="BGR")

        matched_bar.markdown(
            progress_bar(prob),
            unsafe_allow_html=True,
        )

        score_placeholder.metric(label="Score",value=score)

        if prob == 100:
            st.balloons()
            score += 10
            prob =0
            st.session_state["test"] = random.randint(0, NUM_ALPHABETS - 1)
            score_placeholder.metric(label="Score",value=score,delta=10)
            time.sleep(2)


cap.release()
cv2.destroyAllWindows()
