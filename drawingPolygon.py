#-*-coding:utf8-*-

import numpy as np
import cv2

#create a black image
img = np.zeros((512,512,3),np.uint8)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
img = cv2.polylines(img,[pts],True,(0,255,255))

cv2.imshow("polygon",img)
cv2.waitKey(0)