import pickle
import mediapipe as mp
import cv2
import numpy as np
import streamlit as st

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

threshold = 0.7

# model_dict = pickle.load(open("model.p", "rb"))
# model = model_dict["model"]

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']

model_dic = {   # missing Q Z
    'A': 1,
    'B': 1,
    'C': 3,
    'D': 1,
    'E': 1,
    'F': 1,
    'G': 3,
    'H': 3,
    'I': 3,
    'J': 3,
    'K': 1,
    'L': 1,
    'M': 2,
    'N': 3,
    'O': 3,
    'P': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 3,
    'V': 3,
    'W': 3,
    'X': 3,
    'Y': 2
}

action_dir1 = ['A', 'B', 'C', 'D', 'E', 'F', 'K', 'L', 'S']
action_dir2 = ['G', 'I', 'M', 'P', 'R', 'T', 'V', 'Y']
action_dir3 = ['A', 'C', 'G', 'H', 'I', 'J', 'N', 'O', 'U', 'V', 'W', 'X']

model_dict1 = pickle.load(open('./ABCDEFKLS.p', 'rb'))
model_dict2 = pickle.load(open('./GIMPRTVY.p', 'rb'))
model_dict3 = pickle.load(open('./ACGHIJNOUVWX.p', 'rb'))

threshold1 = 0.75
threshold2 = 0.7
threshold3 = 0.7

model1 = model_dict1['model']
model2 = model_dict2['model']
model3 = model_dict3['model']


hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3)

def prediction_model(frame, char):
    data_aux = []
    x_list = []
    y_list = []

    to_guess = char

    frameFlipped = cv2.flip(frame, 1)

    if frame is not None:
        Height, Width, _ = frame.shape  # get (Height, width) of frame

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameFlipped_rgb = cv2.cvtColor(frameFlipped, cv2.COLOR_BGR2RGB)
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

            model_num = model_dic[to_guess]

            if model_num == 1:
                prediction = model1.predict([np.asarray(data_aux)])
                prediction_prob = model1.predict_proba([np.asarray(data_aux)])
                threshold = threshold1
                action_dir = action_dir1

            elif model_num == 2:
                prediction = model2.predict([np.asarray(data_aux)])
                prediction_prob = model2.predict_proba([np.asarray(data_aux)])
                threshold = threshold2
                action_dir = action_dir2

            elif model_num == 3:
                prediction = model3.predict([np.asarray(data_aux)])
                prediction_prob = model3.predict_proba([np.asarray(data_aux)])
                threshold = threshold3
                action_dir = action_dir3

            prob = np.max(prediction_prob)

            if prob > threshold:
                if prediction == to_guess:
                    prob = 100
            else:
                relative_index = action_dir.index(to_guess)
                prob = (
                    int(prediction_prob[0][relative_index] * 100) // 10
                ) * 10

        frameFlipped = cv2.resize(frameFlipped, (450, 350), fx=0.1, fy=0.1, interpolation=cv2.INTER_CUBIC)
    return frameFlipped, prob
