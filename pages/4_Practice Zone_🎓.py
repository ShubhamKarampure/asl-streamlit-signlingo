import cv2
import streamlit as st
import time
from model import prediction_model
import random


if "page" not in st.session_state or st.session_state["page"] != "testpage":
    cv2.destroyAllWindows()
    st.session_state["page"] = "testpage"
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

def hide_streamlit_style():
    return """
        <style>

        .st-emotion-cache-uf99v8 {
            display: flex;
            flex-direction: column;
            width: 100%;
            overflow: auto;
            -webkit-box-align: center;
            align-items: center;
            overflow-clip-margin: content-box;
            overflow: clip;
        }

        /* Hide side toolbar buttons*/
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }

        /* hide header */
        header {
        visibility: hidden;
        height: 0%;
        }

        img {
        border-radius: 1rem;
        }

        .st-emotion-cache-gh2jqd {
            width: 100%;
            padding: 0rem 1rem 10rem;
            max-width: 46rem;
        }

        .st-as {
            height:2rem
        }

        .letterToFind {
            font-size: 200px;
            color: #683aff;
            max-height: 16rem;
            text-align : center;
        }
        </style>
    """


st.markdown(hide_streamlit_style(), unsafe_allow_html=True)

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
    score_placeholder = st.empty()
    charachter_placeholder = st.empty()  # to display video
with col2:
    webcam_placeholder = st.empty()  # to display webcam
    matched_placeholder = st.empty()


# creating the progress bar
prob = 0
score = 0
pred_conf = st.progress(score)

while True and st.session_state.page == "testpage":

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
        matched_placeholder.subheader(f"Matched : {prob}%")
        score_placeholder.subheader(f"Score:{score}")
        pred_conf.progress(score)

        if prob == 100:
            st.balloons()
            score += 10
            st.session_state["test"] = random.randint(0, NUM_ALPHABETS - 1)

            time.sleep(2)


cap.release()
cv2.destroyAllWindows()
