import numpy as np
import cv2
import random
from cv2 import *
import math


#global
canvas = np.ones([500,500,3],'uint8') * 255

cam = cv2.VideoCapture(0)
_,canvas = cam.read()
cam.release()

img = canvas.copy()

font = cv2.FONT_HERSHEY_SIMPLEX

color = (0,255,0)
line_width = -1
radius = 5
point = (0,0)

def line(canvas, point):
    cv2.circle(canvas,point,radius,color,line_width)

def circle(canvas,point,radius):
    cv2.circle(canvas,point,radius,color,8)
    

adjust = False

#click callback
def click(event,x,y,flags,param):
    global canvas, point,pressed,x1,y1,control,radius,adjust, canvas2, text
    if event == cv2.EVENT_LBUTTONDOWN:
        print("LBUTTONDOWN")
        pressed = True
        if control == 'line':
            line(canvas,(x,y))
        if control == 'circle':
            x1,y1 = x,y
            radius = int(math.hypot(x - x1,y - y1))
            circle(canvas,(x1,y1),radius)
    elif event == cv2.EVENT_MOUSEMOVE and pressed == True:
        print("MOUSEMOVE")
        if control == 'line':
            line(canvas,(x,y))  
        if control == 'circle':
            if adjust is True:
                a,b = x,y
                if a !=x and b !=y:
                    canvas = canvas2.copy()
                    radius = int(math.hypot(x - x1, y - y1))
                    circle(canvas,(x1,y1),radius)
    elif event == cv2.EVENT_LBUTTONUP:
        print("LBUTTONUP")
        pressed = False
        if control == 'circle':
           radius = int(math.hypot(x - x1, y - y1))
           circle(canvas,(x1,y1),radius)
           canvas2 = canvas.copy()

#install window and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas",click)        

while True:
        
    
    cv2.imshow("canvas", canvas)
    
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
    if ch & 0xFF == ord('s'):
        canvas = img
        img = canvas.copy()
    if ch & 0xFF == ord('r'):
        color = [0,0,255]
    if ch & 0xFF == ord('b'):
        color = [255,0,0]
    if ch & 0xFF == ord('g'):
        color = [0,255,0]
    if ch& 0xFF == ord('l'):
        control = 'line'
    if ch&0xFF == ord('c'):
        control = 'circle'
    if ch&0xFF == ord('x'):
        adjust = not adjust
    if ch&0xFF == ord('+'):
        radius +=1
    if ch&0xFF == ord('-'):
        radius -=1

    

    