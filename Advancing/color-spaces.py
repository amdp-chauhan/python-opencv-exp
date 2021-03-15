import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('../Resources/Photos/lady.jpg')
cv.imshow('Pretty Lady:',img)

# HSV (Hue-Saturation-Value) format
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV color',hsv_img)

# Grey color space
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey color',grey_img)

# LAB color space
lab_img = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB color',lab_img)

# RGB color space (using matplotlib)
plt.imshow(img)
plt.show()
# result is BGR conversion to RGB -- means Red and Blue are inverted, because of default format in matplotlib

# RGB conversion using OpenCV
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("OpenCV RGB:",rgb_img)

# Show RGB using matplotlib
plt.imshow(rgb_img)
plt.show()

# it's only a matter of default format in these libraries

# Conversion from HSV to BGR
# Conversion from LAB to BGR
# Can't convert from grey to colour

cv.waitKey(0)

