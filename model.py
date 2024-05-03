import pickle
import mediapipe as mp
import cv2
import numpy as np
import streamlit as st

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

threshold = 0.5

model_dict = pickle.load(open("model.p", "rb"))
model = model_dict["model"]

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

word = []


def prediction_model(frame,charachter_index):
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

            prediction = model.predict([np.asarray(data_aux)])
            prediction_prob = model.predict_proba([np.asarray(data_aux)])
            prob = np.max(prediction_prob)

            if prediction_prob[0][charachter_index] > 0.6:
                prob = 100
            else:
                prob = (
                    int(prediction_prob[0][charachter_index] * 100) // 10
                ) * 10

    return frameFlipped, prob
