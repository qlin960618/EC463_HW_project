import io
import time
import picamera

camera=picamera.PiCamera()
camera.start_preview()
camera.framerate = 60

camera.start_recording('./video.h264')
time.sleep(30)
camera.stop_recording()
camera.stop_preview()
