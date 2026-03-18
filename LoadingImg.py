import cv2 as cv   

img = cv.imread('Extra/123.jpeg')
cv.imshow('123',img)
cv.waitKey(0)
#wait key is the amount of time the image is shown for

#when dimenstions of image are greater than the dimentions of the display the image shown is chopped
#since OpenCV has no way of handeling this