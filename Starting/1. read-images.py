import cv2 as cv

img = cv.imread('../Resources/book.jpg')
cv.imshow('Imagege', img)
cv.waitKey(0)