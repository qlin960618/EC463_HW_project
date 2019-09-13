import picamera
import time
import cv2
import os
import io
from picamera.array import PiRGBArray

VIDEO_NAME="./samplevid.avi"
WIDTH=720
HEIGHT=480
NUM_FRAME=300


if(os.path.exists(VIDEO_NAME)):
	os.remove(VIDEO_NAME)

print("enable camera")
camera=picamera.PiCamera()
rawCapture = PiRGBArray(camera)

#camera.start_preview()
time.sleep(2)

print("get recording dimension")
camera.capture(rawCapture, format="bgr")
temp=rawCapture.array
height, width, layers = temp.shape

print("width:%d height:%d"%(width, height))

print("initialize video stream")
video = cv2.VideoWriter(VIDEO_NAME, 0, 1, (width, height))

print("begin capture..")
"""
for i in range(NUM_FRAME):
	print("Num %d Frame"%i)
	camera.capture(rawCapture, format="bgr")
	time.sleep(0.05)
	image = rawCapture.array
	#camera.capture('./image.jpg')
	video.write(image)
"""
stream = io.BytesIO()

frcnt=0
for frame in camera.capture_continuous(stream, format="bgr",  use_video_port=True):
	frcnt=frcnt+1
	image = frame.array
	time.sleep(0.05)
	video.write(image)
	if(frcnt>=NUM_FRAME):
		break





video.release()
#camera.stop_preview()
