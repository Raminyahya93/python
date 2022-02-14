import cv2
import numpy as np
from sklearn.metrics import pairwise

cap = cv2.VideoCapture(0)
kernelopen = np.ones((5,5))
kernelclose = np.ones((20,20))
lb = np.array([20,100,100])
ub = np.array([120,255,255])

while True:
    ret, frame = cap.read()
    flipped = cv2.flip(frame, 1)
    flipped = cv2.resize(flipped,(500,400))
    
    imgseg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imgsegflipped = cv2.flip(imgseg, 1)
    imgsegflipped = cv2.resize(imgsegflipped,(500,400))
    
    mask = cv2.inRange(imgsegflipped, lb ,ub)
    mask = cv2.resize(mask,(500,400))
    
    maskopen = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelopen)
    maskopen = cv2.resize(maskopen,(500,400))
    maskclose = cv2.morphologyEx(maskopen, cv2.MORPH_CLOSE, kernelclose)
    maskclose = cv2.resize(maskclose,(500,400))
    
    final = maskclose , conts, h = cv2.findContours(maskclose,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    if(len(conts)!=0):
        b = max(conts, key=cv2.contourArea)
        west = tuple(b[b[:, :, 0].argmin()][0])
        east = tuple(b[b[:, :, 0].argmax()][0])
        north = tuple(b[b[:, :, 1].argmin()][0])
        south = tuple(b[b[:, :, 1].argmax()][0])
        centre_x = (west[0] + east[0])/2
        centre_y = (north[0] + south[0])/2
        
    cv2.imshow('video',flipped)
    
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break
    
cap.release()
cv2.destroyAllWindows()