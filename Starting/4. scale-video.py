import cv2 as cv

def rescale_frame(frame, scale=0.8):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    new_dim = (width, height)
    return cv.resize(frame, new_dim, interpolation=cv.INTER_AREA)


# Give video file path, in case you want to load that
# vid_capture = cv.VideoCapture(0)
vid_capture = cv.VideoCapture('../Resources/Videos/kitten.mp4')
print(vid_capture.isOpened())

while True:
    is_true, vid_frame = vid_capture.read()
    print(is_true)
    if is_true:
        cv.imshow('Videoeo', rescale_frame(vid_frame, 0.5))
        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

vid_capture.release()
cv.destroyAllWindows()
