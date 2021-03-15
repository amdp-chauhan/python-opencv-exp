import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

lady_img = cv.imread('../Resources/Photos/lady.jpg')
# cv.imshow('Lady:',lady_img)
group1_img = cv.imread('../Resources/Photos/group 1.jpg')
# cv.imshow('Group 1:',group1_img)
group2_img = cv.imread('../Resources/Photos/group 2.jpg')
# cv.imshow('Group 2:',group2_img)

grey_lady_img = cv.cvtColor(lady_img, cv.COLOR_BGR2GRAY)
grey_g1_img = cv.cvtColor(group1_img, cv.COLOR_BGR2GRAY)
grey_g2_img = cv.cvtColor(group2_img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('../Resources/data/haar-face-default.xml')

lady_face_rect = haar_cascade.detectMultiScale(grey_lady_img, scaleFactor=1.1, minNeighbors=2)
g1_face_rect = haar_cascade.detectMultiScale(grey_g1_img, scaleFactor=1.1, minNeighbors=2)
g2_face_rect = haar_cascade.detectMultiScale(grey_g2_img, scaleFactor=1.1, minNeighbors=2)


for (x, y, w, h) in lady_face_rect:
    cv.rectangle(lady_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

for (x, y, w, h) in g1_face_rect:
    cv.rectangle(group1_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

for (x, y, w, h) in g2_face_rect:
    cv.rectangle(group2_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow(f"{len(lady_face_rect)} Detected Faces:", lady_img)
cv.imshow(f"{len(g1_face_rect)} Detected Faces:", group1_img)
cv.imshow(f"{len(g2_face_rect)} Detected Faces:", group2_img)

cv.waitKey(0)