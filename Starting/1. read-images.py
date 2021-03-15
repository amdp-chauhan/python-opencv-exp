import cv2 as cv

img = cv.imread('../Resources/book.jpg')
cv.imshow('Image::', img)
cv.waitKey(0)