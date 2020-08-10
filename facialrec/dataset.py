import numpy as np

import cv2
from cv2 import *

cam = cv2.VideoCapture(0)


haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while True:
    _,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = haar_face_cascade.detectMultiScale(gray,scaleFactor=1.3, minNeighbors = 7)
    for (x,w,y,h) in faces:
        cv2.rectangle(img,(x,y), (x + w, y + h), (0,255,0),2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)
    
    cv2.imshow("Frame" , img)    
    ch = cv2.waitKey(100)
    if ch& 0xFF == ord('q'):
        break
    elif count >=30:
        break
    
        
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()