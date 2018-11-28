import numpy as np
import sys
import cv2 

ball_cascade = cv2.CascadeClassifier('train/cascade.xml')

videoname = sys.argv[1]+'.avi'
cap = cv2.VideoCapture(videoname)

while(True):
    ret, frame = cap.read()

    if ret==False:
    	break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ball = ball_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in ball:
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('ball_detection',frame)

    cv2.waitKey(0)
    

cv2.destroyAllWindows()

