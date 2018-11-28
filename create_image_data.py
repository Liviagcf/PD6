'''
Para rodar tem que rodar o programa com o nome do video como argumento (sem .avi)

Para fazer um positivo clique e arraste fazendo um triangulo em volta da bola e aperte em 'p'

Para fazer um negativo aperte 'n'

Para pular o frame aperte outra tecla
'''



import numpy as np
import sys
import cv2 

cropping = False
 
def click_and_drop(event, x, y, flags, param):

	global refPt, cropping

	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
 
	elif event == cv2.EVENT_LBUTTONUP:
		refPt.append((x, y))
		cropping = False
 
		cv2.rectangle(frame, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("cut", frame)

################################## main #######################################
videoname = sys.argv[1]+'.avi'
cap = cv2.VideoCapture(videoname)

file_positive = open("positive.info","w")
file_negative = open("negative.txt","w")

i = 0

while(True):
    ret, frame = cap.read()
    refPt = []
    i=i+1

    if ret==False:
    	break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)

    imagename = sys.argv[1]+'_'+str(i)+'.png'

    cv2.setMouseCallback('frame', click_and_drop, refPt) 

    option = cv2.waitKey(0)

    if option == ord('p'):
    	print("positive")
    	cv2.imwrite(imagename, gray)
    	file_positive_line = imagename + ' ' + str(1) + ' ' + str(refPt[0][0]) + ' ' + str(refPt[0][1]) + ' ' + str(refPt[1][0]-refPt[0][0])+ ' ' + str(refPt[1][1]-refPt[0][1]) + '\n'
    	file_positive.write(file_positive_line)
    	cv2.destroyWindow("cut")

    elif option == ord('n'):
    	print("negative")
    	cv2.imwrite(imagename, gray)
    	file_negative_line = imagename + '\n'
    	file_negative.write(file_negative_line)



file_positive.close()
file_negative.close()     

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
