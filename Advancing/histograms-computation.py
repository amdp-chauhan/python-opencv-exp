import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def draw_hist(grey_hist, additional_title):
    plt.plot(grey_hist)
    plt.title("Greyscale Histogram "+additional_title)
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.xlim([0, 256])
    plt.show()

img = cv.imread('../Resources/Photos/group 2.jpg')
img = cv.resize(img, (int(img.shape[1]*0.7), int(img.shape[0]*0.7)), interpolation=cv.INTER_AREA)
cv.imshow(f'Group: {img.shape} ',img)


# Histogram - 
# Basically gives the overview of the px distribution

grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey image: ',grey_img)

# Plot histogram
grey_hist = cv.calcHist([grey_img], [0], None, [256], [0,256])
# visualize histogram
# draw_hist(grey_hist, '')
# Since image is mostly white so we have a left skewed distribution

# we can actually just focus on the selected part of the image
blank_img = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank img : ', blank_img)

rect_mask = cv.rectangle(blank_img, (20, 280), (430, 450), (200, 140, 150), thickness=-1)
masked_img = cv.bitwise_and(grey_img, grey_img, mask=rect_mask)
cv.imshow("rectangle mask: ", masked_img)
# visualize histogram
grey_hist = cv.calcHist([grey_img], [0], masked_img, [256], [0,256])

# draw_hist(grey_hist, 'Masked')


# Histogram computation for color image BGR
masked_bgr_img = cv.bitwise_and(img, img, mask=rect_mask)
color_hist = cv.calcHist([img], [0], None, [256], [0,256])

colors = ('b', 'g', 'r')
for i, clr in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=clr)
    plt.xlim([0, 256])

plt.title("Greyscale Histogram BGR Image")
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.show()

cv.waitKey(0)