import cv2
face=cv2.CascadeClassifier("face.xml")
img=cv2.imread("test2.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face.detectMultiScale(gray,1.5,5)
for x,y,w,h in faces:
  new_img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))
cv2.imwrite("img3.jpg",new_img)
