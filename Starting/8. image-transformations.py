import cv2 as cv
import numpy as np

img = cv.imread('../Resources/shapes.png')
cv.imshow('Shapes:',img)

def translate_img(img, x, y):
    trans_matrix = np.float32([[1, 0, x], [0, 1, y]])
    img_dim = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_matrix, img_dim)

# -x : Left
# -y : Up
#  x : Right 
#  y : Down

right_translated = translate_img(img, 100, 0)
cv.imshow('Right Translated', right_translated)
upleft_translated = translate_img(img, -100, -50)
cv.imshow('UpLeft Translated', upleft_translated)

# Rotation
def rotate_img(img, angle, rot_point=None):
    # height, width of a single channel
    (height, width) = img.shape[:2]

    if rot_point is None:
        # Fetching the center of the image
        rot_point = (width//2, height//2)

    rot_matrix = cv.getRotationMatrix2D(rot_point, angle, 1.0)
    img_dim = (width, height)

    return cv.warpAffine(img, rot_matrix, img_dim)    

rotated_img = rotate_img(img, -60)
cv.imshow('Rotated:',rotated_img)


# image resizing
resized_img = cv.resize(img, (400, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized:',resized_img)


# Flipping the image
flipped_img = cv.flip(img, 1)
cv.imshow('Flipped:',flipped_img)


# Cropping the image
cropped_img = img[200:300, 250:400]
cv.imshow('Cropped:', cropped_img)
 
cv.waitKey(0)