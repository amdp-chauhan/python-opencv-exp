import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/group 1.jpg')
cv.imshow('Group:',img)


blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle:',rectangle)
cv.imshow('Circle:',circle)

# Basic bitwise operators

# Bitwise AND
bit_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND:', bit_and)

# Bitwise OR
bit_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR:', bit_or)

# Bitwise NOT
bit_not = cv.bitwise_not(bit_or)
cv.imshow('Bitwise NOT:', bit_not)

# Bitwise XOR
bit_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR:', bit_xor)

cv.waitKey(0)