import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Pretty Lady:',img)

b_img, g_img, r_img = cv.split(img)
cv.imshow(f'Blue Image:{b_img.shape} ',b_img)
cv.imshow(f'Green Image:{g_img.shape} ',g_img)
cv.imshow(f'Red Image:{r_img.shape} ',r_img)

merged_img = cv.merge([b_img, g_img, r_img])
cv.imshow(f'Merged Image:{merged_img.shape} ',merged_img)

# considering all shapes and minimal channels
blank_img = np.zeros(img.shape[:2], dtype='uint8')
# print blue color channle
blue_channel = cv.merge([b_img, blank_img, blank_img])
green_channel = cv.merge([blank_img, g_img, blank_img])
red_channel = cv.merge([blank_img, blank_img, r_img])
cv.imshow("Blue component:", blue_channel)
cv.imshow("Green component:", green_channel)
cv.imshow("Red component:", red_channel)

cv.waitKey(0)