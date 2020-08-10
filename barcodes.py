import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
from cv2 import *

def rescale_frame(frame, percent = 75):
    width = int(frame.shape[1] * percent/100)
    height =int(frame.shape[0] * percent/100)
    dim = (width,height)
    return cv2.resize(frame,dim,interpolation = INTER_AREA)


path = 'qr-code.png'
image = cv2.imread(path)
# cv2.imshow('Image',nparray)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

barcodes = pyzbar.decode(image)

for barcode in barcodes:
    #extract the boundary box location of the barcode and draw the 
    #bounding box surrounding the barcode on the image
    (x,y,w,h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    #draw out barcode output in format we want.
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type
    
    #draw the barcode data
    text =  "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image,text,(x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    
    #print barcode
    print("[INFO] Found {} barcode: {}".format(barcodeType,barcodeData))
    


image = rescale_frame(image,25)
cv2.imshow("Image", image)
cv2.waitKey(0)
        
    
    
