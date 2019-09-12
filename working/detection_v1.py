#import the nesessary library
import time
import os
import io
import picamera
import cv2
import numpy as np

WIDTH=640

HEIGHT=480
DET_WIDTH=300

FPS=10
CAP_DEV="cv2"


VIDEO_NAME="./record.avi"

duration = 1000  #in frames


if os.path.exists(VIDEO_NAME):
	os.remove(VIDEO_NAME)

if CAP_DEV=="PiC":
	#image capture from picamera
	print("enable camera")
	camera = picamera.PiCamera()
	rawCapture = PiRGBArray(camera)
if CAP_DEV=="cv2":
	#image capture crom cv2
	print("enable camera from cv2")
	camera=cv2.VideoCapture(0)

print("start recorder")
videoRec = cv2.VideoWriter(VIDEO_NAME, 0, 1, (WIDTH, HEIGHT))

#print("get recording dimension")
#camera.capture(rawCapture, format="bgr")
#temp=rawCapture.array
#height, width, layers = temp.shape

print("loading classifier file")
car_cascade = cv2.CascadeClassifier('sideviewCar.xml')
#car_cascade = cv2.CascadeClassifier('cars.xml')

#begin capture
print("Begin capture")
for i in range( int(duration/FPS) ):
	carCount=0
	for j in range(FPS):
		if CAP_DEV=="PiC":
			camera.capture(raw, format="bgr")
		if CAP_DEV=="cv2":
			ret, raw = camera.read()
		#convert to grey for less computation
		gray = cv2.cvtColor(raw, cv2.COLOR_BGR2GRAY)

		print("Processing f%d"%j)
		#processing Frame
		cars = car_cascade.detectMultiScale(gray, 1.1, 3)

		for (x, y, w, h) in cars:
			cv2.rectangle(raw, (x, y), (x+w, y+h), (0,255,0), 2)
			print("visible car at: %d %d"%(x+w/2, y+h/2))
			#if ((x+w/2)<(HEIGHT+DET_WIDTH/2))and((x+w/2)>(HEIGHT-DET_WIDTH/2)):
			carCount=carCount+1
		#write to video file
		videoRec.write(raw)

		#delay vid
		#time.sleep(1.0/FPS-0.06)
	print("Second %d, Car count: %d"%(i, carCount))

camera.release()
videoRec.release()

