import cv2

# read image
img = cv2.imread("Image/123.jpeg")

print("Shape:", img.shape)
print("Height:", img.shape[0])
print("Width:", img.shape[1])
print("Channels:", img.shape[2])

#channel - represent how many values are used per pixel to show any color of an image

# print(img)
# print(type(img))