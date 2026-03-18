import cv2 as cv

capture = cv.VideoCapture('Extra/243334.mp4')
capture = cv.VideoCapture(0)
#passing the path of the video file shows the video
#passing 0,1... selects the webcam and shows the thing from the webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()