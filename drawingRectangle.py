#-*-coding:utf8-*-

import numpy as np
import cv2

#create a black image
img = np.zeros((512,512,3),np.uint8)

img = cv2.rectangle(img,(340,0),(510,128),(0,255,0),3)

cv2.imshow("rectangle",img)
cv2.waitKey(0)