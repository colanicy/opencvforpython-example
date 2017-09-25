#-*-coding:utf8-*-

import numpy as np
import cv2

#create a black image
img = np.zeros((512,512,3),np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,0,255),2,cv2.LINE_AA)

cv2.imshow("putText",img)
cv2.waitKey(0)