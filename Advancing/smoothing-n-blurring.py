import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Group:',img)

# Averaging - corner of the sliding window pixel gets averaged to produce the middle pixel
average_blur_img = cv.blur(img, (3, 3))
cv.imshow('Average Blur:',average_blur_img)

# Median Blur - removing salt & pepper noise
median_blur_img = cv.medianBlur(img, 3)
cv.imshow('Median Blur:',median_blur_img)

# Gausian Blurring - weighted average approach of simple averaging
gaus_blur_img = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur:',gaus_blur_img)

# Bilateral Blurring - modern blurring method (retains edges of the image)
bilateral_blur_img = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow('Bilateral Blur:',bilateral_blur_img)


cv.waitKey(0)
