import cv2 as cv

img = cv.imread('../Resources/book.jpg')

def rescale_frame(frame, scale=0.8):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)

    new_dim = (width, height)
    return cv.resize(frame, new_dim, interpolation=cv.INTER_AREA)

cv.imshow('Image::', rescale_frame(img, 0.5))

cv.waitKey(0)