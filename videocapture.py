#-*-coding:utf-8-*-

import cv2
import sys

camID = 0

capture = cv2.VideoCapture(0)
cv2.namedWindow("camera",1)

#set FRAME_WIDTH,FRAME_HEIGHT
'''
设置摄像机分辨率的问题。
最小分辨率，宽度为4，高度为3。
以此类推应该为4的倍数或3的倍数。
你可以通过videocapture成员函数set来设置，摄像机的分辨率。
videocapture默认的情况下为640×480。
'''
print capture.set(3,320)
print capture.set(4,240)

if not capture.isOpened():
	print("Camera open failed!")
	print("Please inspect your camera deviceID %d."%camID)
	sys.exit()

print("capture's props")
content_str = '''CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds or video capture timestamp.
CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file: 0 - start of the film, 1 - end of the film.
CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
CV_CAP_PROP_FPS Frame rate.
CV_CAP_PROP_FOURCC 4-character code of codec.
CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
CV_CAP_PROP_HUE Hue of the image (only for cameras).
CV_CAP_PROP_GAIN Gain of the image (only for cameras).
CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
CV_CAP_PROP_WHITE_BALANCE_U The U value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_WHITE_BALANCE_V The V value of the whitebalance setting (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_ISO_SPEED The ISO speed of the camera (note: only supported by DC1394 v 2.x backend currently)
CV_CAP_PROP_BUFFERSIZE Amount of frames stored in internal buffer memory (note: only supported by DC1394 v 2.x backend currently)
'''
res = content_str.splitlines()

for i in range(0,21):
	key = res[i].split()[0]
	print("--------")
	print(key,":",capture.get(i))
	print(res[i][len(key):])

while(True):
	ha,img = capture.read()
	
	cv2.rectangle(img,(426,0),(640,250),(170,170,0),3)
	cv2.imshow("camera",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

ha,img = capture.read()
print "ha"
print ha
print "img"
print img

capture.release()
cv2.destroyAllWindows()
