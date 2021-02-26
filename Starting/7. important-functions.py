import cv2 as cv

img = cv.imread('../Resources/lena.png')
cv.imshow('Original Image:', img)

# Grey image
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Image:', grey_img)

# Blur
blur_img = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur Image:', blur_img)

# Edge Cascade
canny = cv.Canny(blur_img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dialating the image
dilated = cv.dilate(img, (9,9), iterations=3)
cv.imshow('Dialated..', dilated)

# Eroding
eroded = cv.erode(dilated, (9,9), iterations=3)
cv.imshow('Eroded..', eroded)

# Resize
resized = cv.resize(img, (800, 800), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized:', resized)

# Cropping
cropped_img = img[100:250, 250:400]
cv.imshow('Cropped img:', cropped_img)

cv.waitKey(0)

