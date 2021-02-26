import cv2 as cv

# Give video file path, in case you want to load that
# vid_capture = cv.VideoCapture(0)
vid_capture = cv.VideoCapture('../Resources/Videos/kitten.mp4')
print(vid_capture.isOpened())

while True:
    is_true, vid_frame = vid_capture.read()
    print(is_true)
    if is_true:
        cv.imshow('Videoeo', vid_frame)
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

vid_capture.release()
cv.destroyAllWindows()
