from WebcamVideoStream import WebcamVideoStream
import numpy as np
import cv2
import sys, getopt
import threading
from threading import Thread, Lock
import RPi.GPIO as GPIO
import os
import time

nCameras = 0
cap = [0]*(nCameras+1)
out = [0]*(nCameras+1)
	
picturecount = 0
videocount = 0

fps = 8
width = 640
height = 480

mutex = Lock()

def readVideo(cap):
	frame = [0]*(nCameras+1)
	for i in range(0,nCameras):
		frame[i] = cap[i].read()
	return frame

def writeVideo(frame):
	global out
	for i in range(0,nCameras):
		out[i].write(frame[i])
		
def recordVideo(fps):
	global cap
	if(GPIO.input(4)):
		t = threading.Timer(1.0/fps, recordVideo,[fps])
		t.daemon = True
		t.start()
		frame = readVideo(cap)
		mutex.acquire()
		writeVideo(frame)
		mutex.release()	
	else:
		new_VideoWriters()
		recording = False
	
def take_picture():
	global frame, cap, nCameras, picturecount
	for i in range(0,nCameras):
		frame[i] = cap[i].read()
	for i in range(0,nCameras):
		cv2.imwrite('picture'+str(picturecount)+'_'+str(i)+'.png', frame[i])
				

def new_VideoWriters():
	global out, videocount
	for i in range(0,nCameras):
		out[i] = cv2.VideoWriter('video'+str(videocount)+'_'+str(i)+'.avi', fourcc, fps, (width,height))
		print ('New video')
	videocount += 1

def main(argv):

	global nCameras
	global cap, picturecount, fourcc
	
	try:
		opts, args = getopt.getopt(argv,"hn:")
	except getopt.GetoptError:
		print 'record.py -n <number_of_cameras>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'record.py -n <number_of_cameras>'
			sys.exit()
		elif opt in ("-n"):
			nCameras = int(arg)
	
	if nCameras == 0:
		print 'record.py -n <number_of_cameras>'
		sys.exit()

		
	#Setup GPIO-pins
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	#Picture input-pin
	GPIO.setup(2,GPIO.IN)

	#Start/stop recording input-pin
	GPIO.setup(4,GPIO.IN)
	print ('GPIO set up')

	

	# Create VideoCapture objects
	for i in range(0,nCameras):
		cap[i] = WebcamVideoStream(fps, src=i).start()

	# Define the codec and create VideoWriter objects
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	new_VideoWriters()
	recording = False

	while(1):
		
		#if take picture
		if(GPIO.input(2)):	
			print 'Take picture'
			take_picture()
			picturecount += 1
			time.sleep(1)
			
				
		#if take video
		if(GPIO.input(4)):	
			recording = True
			print 'Start recording'
			recordVideo(fps)
			while(recording):
				pass
			
			
	# Release everything if job is finished
	for i in range(0,nCameras):
		cap[i].stop()
		out[i].release()
	cv2.destroyAllWindows()
	
if __name__ == "__main__":
   main(sys.argv[1:])