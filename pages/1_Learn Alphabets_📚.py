import cv2
import streamlit as st
import time
from model import prediction_model
from urls import video_urls
from components import progress_bar
from styles import page_setup,page_with_webcam_video
import mysql.connector
from Signlingo import current_user
import datetime

print(datetime.datetime.now())
if "page" not in st.session_state or st.session_state["page"]!='learnpage':
    cv2.destroyAllWindows()
    st.session_state["page"] = 'learnpage'
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aj19@SQL",
    database="signlingo"
     )
st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

def update_video(charachter):
    return f"""
    <div class="video-wrapper">
    <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scaleX(-1);">
        <source src="{video_urls[charachter]}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    </div>  
    """

if "alphabet" not in st.session_state:
    st.session_state["alphabet"] = 0

ALPHABET_LIST = ["A", "B", "C", "D", "E", "F","G","H", "I","J","K" "L", "O", "R", "U", "Y"]
NUM_ALPHABETS = len(ALPHABET_LIST)

# Element struction
title_placeholder = st.empty()  # stores letter title
col1, col2 = st.columns([0.5, 0.5])
with col1:
    video_placeholder = st.empty()  # to display video
    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )
with col2:
    webcam_placeholder = st.empty()  # to display webcam

matched_placeholder = st.empty()

# creating the progress bar
prob = 0
progress_bar_placeholder = st.empty()

while True and st.session_state.page == "learnpage":

    if cap is not None or cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:
        title_placeholder.header(
            f"Learning Alphabet : {ALPHABET_LIST[st.session_state['alphabet']]}"
        )

        frame, prob = prediction_model(frame,st.session_state["alphabet"])
        frame = cv2.resize(
            frame, (500, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC
        )
        webcam_placeholder.image(frame, channels="BGR")


        progress_bar_placeholder.markdown(
            progress_bar(prob),
            unsafe_allow_html=True,
        )

        if prob == 100:
            st.balloons()

            video_placeholder.empty()
             # WORD_LIST[current_word_index] # Aroosh
            try:
                    with conn.cursor() as cursor:

                        print(datetime.datetime.now())
                        formatted_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        query = f"insert into learntletter values ('{current_user['username']}','{ALPHABET_LIST[st.session_state['alphabet']]}', '{formatted_datetime}')"
                        cursor.execute(query)
                        conn.commit()
                        print(f"You Learnt the alphabet {st.session_state['alphabet']}" )
    
                        pass
            except Exception as e:
                    print(e)
            
 
               # Aroosh

            print(st.session_state["alphabet"])

            st.session_state["alphabet"] = ( st.session_state["alphabet"] + 1 ) % NUM_ALPHABETS

            time.sleep(2)

            video_placeholder.markdown(
                update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
                unsafe_allow_html=True,
            )

cap.release()
cv2.destroyAllWindows()
conn.close()
