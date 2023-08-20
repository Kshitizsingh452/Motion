import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(1)

mpHands=mp.solutions.hands
hands=mpHands.Hands()



while True:
    success, img = cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGRA2RGB)
    results=hands.process(imgRGB)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:



    cv.imshow("image", img)
    cv.waitKey(0)

