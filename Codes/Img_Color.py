import cv2

# read image
img = cv2.imread("Image/image.png")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#can be used to seperate the background and subject if both have the same color

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#Img color is weird bcs even after converting to RGB it treats the final values/weights as BGR

# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LUV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

#total = 255+255+255
#the way color is calculated - (a,b,c) : a/total + b/total + c/total decides the color of the image

negative = 255 - img

cv2.imshow("Kingfisher", img)
cv2.imshow("Negative", negative)
cv2.waitKey(0)
cv2.destroyAllWindows()