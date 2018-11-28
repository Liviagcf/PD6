import numpy as np
<<<<<<< HEAD
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
=======
import cv2 as cv


face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
img = cv.imread('rostos-misturados.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
>>>>>>> 276816daf656228588a8543dee08651f07ed2480
