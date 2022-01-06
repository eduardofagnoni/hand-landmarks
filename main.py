import cv2
import mediapipe as mp
import time

webcam = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

if webcam.isOpened():
    print("Conectado...")

    validacao, frame = webcam.read()

    while validacao:
        validacao, frame = webcam.read()

        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)


        cv2.imshow("Video", frame)
        key = cv2.waitKey(5)

        if key == 27: #ESC
            break

        
    cv2.imwrite("Foto.png", frame)

webcam.release()
cv2.destroyAllWindows()