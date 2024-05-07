import cv2
import streamlit as st
import time
import sqlite3
from model import prediction_model
from components import progress_bar, update_video,detected_word
from styles import page_setup, page_with_webcam_video


if "page" not in st.session_state or st.session_state["page"]!='wordpage':
    cv2.destroyAllWindows()
    st.session_state["page"] = 'wordpage'


conn = sqlite3.connect("signlingo.db")
c = conn.cursor()

current_user = st.session_state["current_user"]

cap = cv2.VideoCapture(cv2.CAP_DSHOW)

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)


if "word" not in st.session_state:
    st.session_state['word'] = 0
    st.session_state['index'] = 0


WORD_LIST = [
    "CODE",
    "DATA",
    "LEARN",
    "TEST",
    "IDEA",
    "PYTHON",
    "HAPPY",
    "SMART",
    "QUICK",
    "BRAIN",
]
NUM_WORD = len(WORD_LIST)

# Element structure
col1, col2 = st.columns([0.5, 0.5], gap="medium")
with col1:
    video_placeholder = st.empty()  # to display video
    video_placeholder.markdown(
        update_video(
            WORD_LIST[st.session_state["word"]][st.session_state["index"]]
        ),
        unsafe_allow_html=True,
    )
    matched_placeholder = st.empty()
with col2:
    webcam_placeholder = st.empty()  # to display webcam
    progress_bar_placeholder = st.empty()


# creating the progress bar

while True and st.session_state["page"] == "wordpage":

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:

        current_word_index = st.session_state["word"]

        frame, prob = prediction_model(
            frame,
            WORD_LIST[st.session_state["word"]][st.session_state['index']]
        )

        webcam_placeholder.image(frame, channels="BGR")

        matched_placeholder.markdown(
            detected_word(WORD_LIST[current_word_index],st.session_state["index"]-1), unsafe_allow_html=True
        )
        #  print("Printing Manually" +WORD_LIST[current_word_index])

        progress_bar_placeholder.markdown(
            progress_bar(prob),
            unsafe_allow_html=True,
        )

        if prob == 100:
            print()
            st.session_state["index"] += 1
            if st.session_state["index"] == len(
                WORD_LIST[st.session_state["word"]]
            ):

                matched_placeholder.markdown(
                    detected_word(
                        WORD_LIST[current_word_index], st.session_state["index"] - 1
                    ),
                    unsafe_allow_html=True,
                )
                # WORD_LIST[current_word_index] # Aroosh
                try:
                    c.execute(
                        """INSERT INTO Words (username, word) VALUES (?, ?)""",
                        (current_user["username"], WORD_LIST[st.session_state["word"]]),
                    )
                    print("added_letter")
                    conn.commit()
                    pass
                except Exception as e:
                    print(e)

                # Aroosh
                st.session_state["index"] = 0
                st.session_state["word"] = (st.session_state["word"] + 1) % NUM_WORD
                st.balloons()

            video_placeholder.empty()

            time.sleep(2)
            matched_placeholder.empty()
            video_placeholder.markdown(
                update_video(
                    WORD_LIST[st.session_state["word"]][st.session_state["index"]]
                ),
                unsafe_allow_html=True,
            )

cap.release()
cv2.destroyAllWindows()
conn.close()
