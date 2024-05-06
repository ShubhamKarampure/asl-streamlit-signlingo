import cv2
import streamlit as st
import time
from model import prediction_model
from urls import video_urls
from components import progress_bar
from styles import page_setup, page_with_webcam_video
import mysql.connector
from Signlingo import current_user
import datetime

if "page" not in st.session_state or st.session_state["page"]!='wordpage':
    cv2.destroyAllWindows()
    st.session_state["page"] = 'wordpage'
    

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aj19@SQL",
    database="signlingo"
     )



cap = cv2.VideoCapture(cv2.CAP_DSHOW)

st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)




def update_video(character):
    return f"""
    <div class="video-wrapper">
    <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scaleX(-1);">
        <source src="{video_urls[character]}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    </div>  
    """


def detected_word(WORD, detected_index):
    markdown_str = f'<div style="font-family: Arial, sans-serif; font-weight: bold; text-align: center; font-size: 30px;">'
    # Loop through each letter in the word
    for i, letter in enumerate(WORD):
        # Check if the current letter index is less than or equal to the detected index
        if i <= detected_index:
            # If yes, add the letter in green color
            markdown_str += f'<span style="color:#ffe090;">{letter}</span>'
        else:
            # If no, add the letter in white color
            markdown_str += f'<span style="color:white;">{letter}</span>'
    markdown_str += "</div>"
    return markdown_str


if "word" not in st.session_state:
    st.session_state['word'] = 0
    st.session_state['index'] = 0

WORD_LIST = ["ABC"]
NUM_WORD = len(WORD_LIST)

# Element structure
title_placeholder = st.empty()  # stores letter title
col1, col2 = st.columns([0.5, 0.5], gap="medium")
with col1:
    video_placeholder = st.empty()  # to display video
    video_placeholder.markdown(
        update_video(
            WORD_LIST[st.session_state["word"]][st.session_state["index"]]
        ),
        unsafe_allow_html=True,
    )
with col2:
    webcam_placeholder = st.empty()  # to display webcam

matched_placeholder = st.empty()

# creating the progress bar
progress_bar_placeholder = st.empty()

while True and st.session_state["page"] == "wordpage":

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:
        title_placeholder.header("Learn Word")
        current_word_index = st.session_state["word"]

        frame, prob = prediction_model(
            frame,
            ord(WORD_LIST[st.session_state["word"]][st.session_state['index']])
            - ord("A"),
        )

        frame = cv2.resize(
            frame, (500, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC
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
                    with conn.cursor() as cursor:
                        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        print(date) 
                        query = f"insert into learntword values ('{current_user['username']}','{WORD_LIST[st.session_state['word']]}','{date}')"
                        cursor.execute(query)
                        conn.commit()
                        print(f"You Learnt the word {WORD_LIST[st.session_state['word']]}" )
    
                        pass
                except Exception as e:
                    print(e)
                finally:
                    conn.close()
 
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
