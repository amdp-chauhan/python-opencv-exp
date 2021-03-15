import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

video_cap = cv.VideoCapture('../Resources/Videos/Marvel Studios\' The Falcon and The Winter Soldier.mp4')

haar_cascade = cv.CascadeClassifier('../Resources/data/haar-face-default.xml')

while True:
    is_true, video_frame = video_cap.read()
    grey_frame = cv.cvtColor(video_frame, cv.COLOR_BGR2GRAY)
    vid_face_rect = haar_cascade.detectMultiScale(grey_frame, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in vid_face_rect:
        cv.rectangle(video_frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    if is_true:
        cv.imshow('Video::', video_frame)
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cv.waitKey(0)