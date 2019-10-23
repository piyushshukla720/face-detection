import cv2
video=cv2.VideoCapture(0)
face=cv2.CascadeClassifier("face.xml")
img=0
while True:
 check, frame=video.read()
 gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 faces=face.detectMultiScale(gray,1.5,5)
 for x,y,w,h in faces:
   img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))
 cv2.imshow("Test",img)
 key=cv2.waitKey(1)
 if key==ord("q"):
   break
video.release()
cv2.destroyAllWindows
