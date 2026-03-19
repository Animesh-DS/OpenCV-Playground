import cv2 as cv

capture = cv.VideoCapture('Image/111.mp4')
#passing the path of the video file shows the video
#passing 0,1... selects the webcam and shows the thing from the webcam

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# in the loop what we do is take and then show a single frame
# the "isTrue" is a bool that checks whether we got a frmae without any problem or not
# oxFF==ord('d') checks if d is pressed end the video showcase

capture.release()
cv.destroyAllWindows()

# when the video ends it shows an  251 Assertion Error - this error means that no file was found at
# the provided location and in our case after the end of the video no frame was present hence
# that issue