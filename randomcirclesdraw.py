import numpy as np
import cv2
import random
from cv2 import *

#global
canvas = np.ones([500,500,3],'uint8') * 255

cam = cv2.VideoCapture(0)
_,canvas = cam.read()
cam.release()
def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


color = (0,255,0)
line_width = 3
radius = 100
point = (0,0)

#click callback
def click(event,x,y,flags,param):
    global canvas, point,pressed,color
    if event == cv2.EVENT_LBUTTONDOWN:
        print("LBUTTONDOWN")
        point = (x,y)
        cv2.circle(canvas,point,radius,color,line_width)
    elif event == cv2.EVENT_MOUSEMOVE:
        print("MOUSEMOVE")
    elif event == cv2.EVENT_LBUTTONUP:
        print("LBUTTONUP")
        color = random_color()


#install window and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)        

while True:
        
    
    cv2.imshow("canvas", canvas)
         
    
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    # canvas = np.ones([500,500,3],'uint8') * 255
        

    