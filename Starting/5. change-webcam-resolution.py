import cv2 as cv

# Only works on Live cam
def change_resolution(vid_capture, width, height):
    vid_capture.set(3, width)
    vid_capture.set(4, height)
    return vid_capture

# Give video file path, in case you want to load that
vid_capture = change_resolution(cv.VideoCapture(0), 680, 480)
print(vid_capture.isOpened())

while True:
    is_true, vid_frame = vid_capture.read()
    print(is_true)
    if is_true:
        cv.imshow('web cam ::', vid_frame)
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

vid_capture.release()
cv.destroyAllWindows()
