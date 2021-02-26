import cv2 as cv
import numpy as np

img = cv.imread('../Resources/lambo.png')
cv.imshow('Lamboo:',img)

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GreyImg:',grey_img)

blur_grey_img = cv.GaussianBlur(grey_img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('BlurGreyImg:', blur_grey_img)

canny_edges = cv.Canny(blur_grey_img, 125, 175)
cv.imshow('Canny Edge:', canny_edges)

# contours obtained on the edges of blurred images are lesser than the original image edges
contours, hierarchies = cv.findContours(canny_edges, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'len of coutours in img edges:{len(contours)}')

# Binary image
ret, thresh = cv.threshold(grey_img, 125, 255, cv.THRESH_BINARY)
cv.imshow('Binary Image:', thresh)

# contours obtained on the binary image
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'len of coutours in img binary thresh:{len(thresh)}')

# Visualizing contours
blank_img = np.zeros(img.shape)

cv.drawContours(blank_img, contours, -1, (0, 255, 0), 1)
cv.imshow('Contour over binary:', blank_img)

cv.waitKey(0)