#-*-coding:utf8-*-

import numpy as np
import cv2

#create a black image
img = np.zeros((512,512,3),np.uint8)

img = cv2.ellipse(img,(256,256),(150,50),15,0,360,(255,0,0),-1)
'''
img 图像
center 椭圆圆心坐标（256，256）
axes 轴的长度（150，50）(major axis length, minor axis length)
angle 偏转的角度 15
start_angle 圆弧起始角的角度 0
end_angle 圆弧终结角的角度 360
color 线条的颜色 (255,0,0)
thickness 线条的粗细程度 -1(表示填充图形)
lint_type 线条类型，见CVLINE的描述
shift 圆心坐标点和数轴的精度
'''

cv2.imshow("ellipse",img)
cv2.waitKey(0)