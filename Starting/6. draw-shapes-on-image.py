import cv2 as cv
import numpy as np

blank_img = np.zeros((600, 600, 3))
cv.imshow('Blank Image', blank_img)

# 1. Colour a rectangular part of the image
blank_img[100:150, 250:300] = 0, 0, 150
blank_img[150:200, 300:350] = 0, 123, 150
blank_img[200:250, 350:400] = 130, 23, 140
cv.imshow('Colour patches', blank_img)

# 2. Draw a Rectangle
cv.rectangle(blank_img, (100,150), (350, 400), (200, 140, 150), thickness=1)
cv.imshow('Random Rectangle', blank_img)

# 3. Draw a Circle
cv.circle(blank_img, (100, 150), 40, (0, 0, 150), thickness=-1)
cv.circle(blank_img, (100, 400), 40, (0, 123, 150), thickness=-1)
cv.circle(blank_img, (350, 400), 40, (130, 23, 140), thickness=-1)
cv.imshow('Random Circle', blank_img)

# 3. Draw a Line
cv.line(blank_img, (100, 150), (350, 400), (200, 0, 0), thickness=3)
cv.line(blank_img, (225, 275), (100, 400), (200, 0, 0), thickness=3)
cv.imshow('Random Line', blank_img)

# 4. Put text on an image
cv.putText(blank_img, ' Joker ', (100, 280), cv.FONT_HERSHEY_TRIPLEX, 0.8, (0, 255, 0), 2)
cv.imshow('Put text', blank_img)

cv.waitKey(0)
