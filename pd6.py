import numpy as np
import sys
import cv2 


def pixelCountCheck(blackMin, whiteMin, whiteMask, blackMask, pt1, pt2):

	height, width = whiteMask.shape
	canvas = whiteMask.copy()
	canvas[0:height, 0:width] = 0

	maskedWhite = canvas.copy()
	maskedBlack = canvas.copy()

	canvas = cv2.rectangle(canvas,pt1,pt2,255,-1)
	maskedWhite = canvas&whiteMask
	maskedBlack = canvas&blackMask

	whiteCount = cv2.countNonZero(maskedWhite)
	blackCount = cv2.countNonZero(maskedBlack)

	area = (pt1[0]-pt2[0])*(pt1[1]-pt2[1])*1.0

	if(whiteCount/area > whiteMin and blackCount/area > blackMin):
		return 1
	else:
		return 0



ball_cascade = cv2.CascadeClassifier('train/cascade.xml')

videoname = sys.argv[1]+'.avi'
cap = cv2.VideoCapture(videoname)

param1 = 0.1
param2 = 0.1

valid = 0

while(True):
    ret, frame = cap.read()

    if ret==False:
    	break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ball = ball_cascade.detectMultiScale(gray, 1.3, 5)

    whiteMask = cv2.inRange(gray, 100, 255)
    blackMask = cv2.inRange(gray, 0, 100)

    for (x,y,w,h) in ball:
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    	valid =  pixelCountCheck(0, 0, whiteMask, blackMask, (x,y),(x+w,y+h))


    cv2.imshow('ball_detection',frame)

    cv2.waitKey(0)
    

cv2.destroyAllWindows()