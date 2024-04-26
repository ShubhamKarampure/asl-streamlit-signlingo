import pickle
import mediapipe as mp
import cv2
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

frame_placeholder = st.empty()
predicted_character_placeholder = st.empty()

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

            cv2.putText(
                frameFlipped,
                prediction[0],
                (x1_Flipped - (x2 - x1), y1_Flipped - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.3,
                (0, 0, 0),
                3,
                cv2.LINE_AA,
            )

            
            predicted_character_placeholder.text(
                    f"Predicted Character: {prediction}"
                )
    return frameFlipped


import cv2

cap = None  # Initialize the video capture instance

while True:
    if cap is None or not cap.isOpened():
        cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        frame = prediction_model(frame)
        frame_placeholder.image(frame, channels="BGR")
