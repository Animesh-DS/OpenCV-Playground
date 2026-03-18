import cv2

# read image
img = cv2.imread("Image/image.png")

cv2.line(img, (540,360), (680, 180), (0, 0, 255), 3)
#line(image,start point, end point, color, thickness)
cv2.line(img,(680,180),(720,180),(0,0,255),3)

cv2.rectangle(img,(720,140),(1000,260),(34,25,50),-1)
#rectangle(image,top left corner,bottom right corner, color, -1 for fill - other no of thickness of border)

cv2.circle(img,(420,140),130,(0,0,0),100)
#cicle(image,orgin,radius,color,thickness)

cv2.putText(img,"Kingfisher",(740,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),10)
#putText(image,text,bottom left corner,font,scale,color,thickness)
cv2.imshow("Line",img)
cv2.waitKey(0)
cv2.destroyAllWindows()