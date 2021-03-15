import cv2 as cv
import numpy as np
import os

# get a list of people img directories (labels)
people = []
FACE_DIR = '../Resources/Faces/train'
for i in os.listdir(FACE_DIR):
    people.append(i)

haar_cascade = cv.CascadeClassifier('../Resources/data/haar-face-default.xml')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('trained-recognizer.yml')

test_img = cv.imread('../Resources/Faces/val/madonna/4.jpg')
grey_test_img = cv.cvtColor(test_img, cv.COLOR_BGR2GRAY)
# Detect the face in the test_img
faces_rect = haar_cascade.detectMultiScale(grey_test_img, 1.1, 4)

# recognize and localize image
for (x, y, w, h) in faces_rect:
    faces_roi = grey_test_img[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)

    cv.putText(test_img, f'{people[label]} ({round(confidence, 1)})', (30, 30), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), thickness=1)
    cv.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)

cv.imshow(f'Detected Image: ',test_img)

cv.waitKey(0)