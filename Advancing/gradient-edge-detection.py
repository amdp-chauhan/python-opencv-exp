import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../Resources/p1.jpg')
img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)), interpolation=cv.INTER_AREA)
cv.imshow(f'Cars: {img.shape} ',img)
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow(f'Grey Car: {grey_img.shape} ',grey_img)

# Laplacian
lap = cv.Laplacian(grey_img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian:',lap)

# Sobel
sobelx = np.uint8(np.absolute(cv.Sobel(grey_img, cv.CV_64F, 1, 0)))
sobely = np.uint8(np.absolute(cv.Sobel(grey_img, cv.CV_64F, 0, 1)))
cv.imshow('Sobel x ',sobelx)
cv.imshow('Sobel y ',sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel ',combined_sobel)

# Canny edge detector
canny_edge_img = cv.Canny(grey_img, 150, 200)
cv.imshow('Canny Edge Img ',canny_edge_img)

cv.waitKey(0)
