import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('../Resources/cards.jpg')
# img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)), interpolation=cv.INTER_AREA)
cv.imshow(f'Group: {img.shape} ',img)

# Simple thresholding
THRESHOLD = 125
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grey img -',grey_img)

thresold, thresh = cv.threshold(grey_img, THRESHOLD, 255, cv.THRESH_BINARY)
cv.imshow('Threshold ',thresh)

# inverse threshold
thresold, inv_thresh = cv.threshold(grey_img, THRESHOLD, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Threshold',inv_thresh)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(grey_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive thresholding:', adaptive_thresh)

cv.waitKey(0)