import cv2
cap=cv2.VideoCapture(0);
while(True):
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#image
'''
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('test.jpg')

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)

cv2.imshow('img',img)
cv2.waitKey()
'''
#video
'''
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture('testv.mp4')
while cap.isOpened():
    _,img=cap.read()
    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('banu',img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cv2.release()
cv2.destroyAllWindows()
'''
