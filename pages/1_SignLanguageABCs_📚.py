import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import time


hide_streamlit_style = """
                <style>
                
                img {
                border-radius: 1rem;
                
                 /* Adjust the thickness and color as needed */
                }


                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stDecoration"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                [data-testid="ScrollToBottomContainer"] {
                 overflow: hidden;
                }
               .st-emotion-cache-gh2jqd {
                    width: 100%;
                    padding: 0rem 1rem 10rem;
                    max-width: 46rem;
                }
                .st-as {
                    height:2rem
                }

                .video-wrapper {
                background-color: white;
                display: inline-block;
                width: 336px;
                height: 336px;
                overflow: hidden;
                position: relative;
                border-radius: 1rem; /* Add border radius to match the image */
                align-content : center
                }

                

            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

video_urls = {
    "A": "https://videos-asl.lingvano.com/9099-480p.mp4",
    "B": "https://videos-asl.lingvano.com/9101-480p.mp4",
    "C": "https://videos-asl.lingvano.com/9102-480p.mp4",
    "D": "https://videos-asl.lingvano.com/9133-480p.mp4",
    "E": "https://videos-asl.lingvano.com/9103-480p.mp4",
    "F": "https://videos-asl.lingvano.com/9131-480p.mp4",
    "G": "https://videos-asl.lingvano.com/9126-480p.mp4",
    "H": "https://videos-asl.lingvano.com/9132-480p.mp4",
    "I": "https://videos-asl.lingvano.com/9115-480p.mp4",
    "J": "https://videos-asl.lingvano.com/9127-480p.mp4",
    "K": "https://videos-asl.lingvano.com/9111-480p.mp4",
    "L": "https://videos-asl.lingvano.com/9134-480p.mp4",
    "M": "https://videos-asl.lingvano.com/9113-480p.mp4",
    "N": "https://videos-asl.lingvano.com/9108-480p.mp4",
    "O": "https://videos-asl.lingvano.com/9109-480p.mp4",
    "P": "https://videos-asl.lingvano.com/9112-480p.mp4",
    "Q": "https://videos-asl.lingvano.com/9124-480p.mp4",
    "R": "https://videos-asl.lingvano.com/9122-480p.mp4",
    "S": "https://videos-asl.lingvano.com/9125-480p.mp4",
    "T": "https://videos-asl.lingvano.com/9120-480p.mp4",
    "U": "https://videos-asl.lingvano.com/9118-480p.mp4",
    "V": "https://videos-asl.lingvano.com/9130-480p.mp4",
    "W": "https://videos-asl.lingvano.com/9116-480p.mp4",
    "X": "https://videos-asl.lingvano.com/9119-480p.mp4",
    "Y": "https://videos-asl.lingvano.com/9128-480p.mp4",
    "Z": "https://videos-asl.lingvano.com/9129-480p.mp4",
}

if "alpbhabet" not in st.session_state:
    st.session_state["alphabet"] = 0

def update_video(charachter):
    return f"""
    <div class="video-wrapper">
    <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scaleX(-1);">
        <source src="{video_urls[charachter]}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    </div>  
    """

action_dic = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "I",
    7: "L",
    8: "O",
    9: "R",
    10: "U",
    11: "Y",
}


prob = 0
charachter_placeholder = st.empty()
col1, col2 = st.columns([0.5,0.5],gap="medium")
with col1:
    video_placeholder = st.empty()
    video_placeholder.markdown(
        update_video(action_dic[st.session_state["alphabet"]]), unsafe_allow_html=True
    )
with col2:
    frame_placeholder = st.empty()
predicted_character_confidence = st.empty()
pred_conf = st.progress(prob)


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

match = 1
threshold = 0.5

model_dict = pickle.load(open("model.p", "rb"))
model = model_dict["model"]

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

word = []


def prediction_model(frame):
    data_aux = []
    x_list = []
    y_list = []

    frameFlipped = cv2.flip(frame, 1)

    if frame is not None:
        Height, Width, _ = frame.shape  # get (Height, width) of frame

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameFlipped_rgb = cv2.cvtColor(frameFlipped, cv2.COLOR_BGR2RGB)
        predicted_char = "."
        prob = 0

        results = hands.process(frame_rgb)
        resultsFlipped = hands.process(frameFlipped_rgb)

        if resultsFlipped.multi_hand_landmarks and results.multi_hand_landmarks:
            for hand_landmarks in resultsFlipped.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frameFlipped,  # image to draw
                    hand_landmarks,  # model output
                    mp_hands.HAND_CONNECTIONS,  # hand connections
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style(),
                )

            if len(results.multi_hand_landmarks) == 2 and len(word) != 0:
                print("".join(word))
                word.clear()

            for hand_landmarks in [results.multi_hand_landmarks[0]]:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    x_list.append(x)
                    y_list.append(y)

                min_x = min(x_list)
                min_y = min(y_list)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    data_aux.append(x - min_x)
                    data_aux.append(y - min_y)

            max_x = max(x_list)
            max_y = max(y_list)

            x1 = int(min_x * Width) - 10
            y1 = int(min_y * Height) - 10

            x2 = int(max_x * Width) + 10
            y2 = int(max_y * Height) + 10

            prediction = model.predict([np.asarray(data_aux)])
            prediction_prob = model.predict_proba([np.asarray(data_aux)])
            prob = np.max(prediction_prob)

            x1_Flipped = Width - x1
            y1_Flipped = y1
            x2_Flipped = Width - x2
            y2_Flipped = y2

            cv2.rectangle(
                frameFlipped,
                (x1_Flipped, y1_Flipped),
                (x2_Flipped, y2_Flipped),
                (0, 0, 0),
                4,
            )

            if prediction_prob[0][st.session_state["alphabet"]] > 0.6:
                prob = 100
            else:
                prob = (int(prediction_prob[0][st.session_state["alphabet"]] * 100) // 10) * 10

    return frameFlipped,prob

if "page" not in st.session_state:
    st.session_state["page"] = "learnpage"
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

if st.session_state["page"] != "learnpage":
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

st.session_state["page"] = "learnpage"

while True and st.session_state.page == "learnpage":

    if cap is not None or cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:
        charachter_placeholder.header(f"Learning Alphabet : {action_dic[st.session_state['alphabet']]}")

        frame,prob = prediction_model(frame)
        frame = cv2.resize(
            frame, (500, 500), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC
        )
        frame_placeholder.image(frame, channels="BGR")
        predicted_character_confidence.subheader(f"Matched : {prob}%")
        pred_conf.progress(prob)

        if prob == 100:
            st.balloons()

            video_placeholder.empty()

            st.session_state["alphabet"] += 1

            time.sleep(2)

            video_placeholder.markdown(
                update_video(action_dic[st.session_state["alphabet"]]), unsafe_allow_html=True
            )

cap.release()
cv2.destroyAllWindows()
