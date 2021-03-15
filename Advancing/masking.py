import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/group 2.jpg')
img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)), interpolation=cv.INTER_AREA)
cv.imshow(f'Group: {img.shape} ',img)
# Shape (579, 448)

# Masking - helps in focusing only the part of the image
blank_img = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank img : ', blank_img)

rect_mask = cv.rectangle(blank_img, (20, 280), (430, 450), (200, 140, 150), thickness=-1)
cv.imshow("rectangle mask: ", rect_mask)

masked_img = cv.bitwise_and(img, img, mask=rect_mask)
cv.imshow("Masked img : ",masked_img)

cv.waitKey(0)