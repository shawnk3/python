import numpy as np

import cv2


cam = cv2.VideoCapture(0)

haar_face = cv2.CascadeClassifier('facecascade.xml')
smile = cv2.CascadeClassifier('smile.xml')


while True:
    
    _,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = haar_face.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 7)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        smiles = smile.detectMultiScale(roi_gray,scaleFactor = 1.1, minNeighbors = 30)
        if len(smiles) > 0: 
            for (ex,ey,ew,eh) in smiles:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.rectangle(roi_color,(ex,ey),(ex + ew, ey+eh), (0,255,0),2)
                cv2.putText(frame, "HAPPY", (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(35,255,12),3)
        else:
            cv2.putText(frame, "SAD", (x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(35,12,255),3)
    
    cv2.imshow('Frame',frame)
    
    ch = cv2.waitKey(1)
    if ch&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()