# write your solution to Exercise W10.T03 here
# import in the matplotlib module
import numpy as np
# inport in the OpenCV module
import cv2


# open camera/capture image
cam = cv2.VideoCapture(0)
_,img = cam.read() # read image from camera
cam.release() #release (close) camera

# draw rectangles of different colors on top of the image
img  = cv2.rectangle(img,(0, 640) ,(480 ,0 ), (255,0,0) , 200)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()