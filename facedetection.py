import numpy as np
import matplotlib as plt
import cv2
from cv2 import *

cam = cv2.VideoCapture(0)
_,img = cam.read()
cam.release()

haar_face_cascade = cv2.CascadeClassifier('facecascade.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = haar_face_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors = 5)
for (x,w,y,h) in faces:
    cv2.rectangle(img,(x,y), (x + w, y + h), (0,255,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color= img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex,ew,ey,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey), (ex + ew, ey + eh), (0,255,0),2)
    
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()