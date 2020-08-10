import numpy as np
import cv2
from cv2 import *


def rescale_frame(frame, percent = 75):
    width = int(frame.shape[1] * percent/100)
    height =int(frame.shape[0] * percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation = INTER_AREA)

img = cv2.imread('faces-1.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]# hue
s = hsv[:,:,1]#saturation
v = hsv[:,:,2]#color

hsv_split = np.concatenate((h,s,v), axis =1)
img = rescale_frame(hsv_split,50)
cv2.imshow('Split HSV', img)

ret, min_sat =cv2.threshold(s,40,255,cv2.THRESH_BINARY)
img = rescale_frame(min_sat,50)
cv2.imshow('Saturation',img)

ret,max_hue = cv2.threshold(h,15,255,cv2.THRESH_BINARY_INV)
img = rescale_frame(max_hue,50)
cv2.imshow('Hue',img)

final = cv2.bitwise_and(min_sat,max_hue)
cv2.imshow('Final',final)

cv2.waitKey(0)





