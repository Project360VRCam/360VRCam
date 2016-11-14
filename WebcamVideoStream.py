# import the necessary packages
from threading import Thread
import cv2
import time
 
class WebcamVideoStream:
	def __init__(self, fps, src=0):
		# initialize the video camera stream and read the first frame
		# from the stream
		self.stream = cv2.VideoCapture(src)
		self.stream.set(cv2.CAP_PROP_FPS, fps)
		(self.grabbed, self.frame) = self.stream.read()
 
		# initialize the variable used to indicate if the thread should
		# be stopped
		self.stopped = False
		self.frame_count = 0
		self.src = src

	def start(self):
		# start the thread to read frames from the video stream
		t = Thread(target=self.update, args=())
		t.daemon = True
		t.start()
		return self
 
	def update(self):
		# keep looping infinitely until the thread is stopped
		while True:
			# if the thread indicator variable is set, stop the thread
			if self.stopped:
				return
 
			# otherwise, read the next frame from the stream
			# and measure fps from camera
			if (self.frame_count == 0):
				self.t = time.clock()
				
			(self.grabbed, self.frame) = self.stream.read()
			self.frame_count += 1
			
			if (self.frame_count == 100):
				self.elapsed_t = time.clock() - self.t
				self.frame_rate = 100/self.elapsed_t
				print "Camera %d fps: %d" %(self.src, self.frame_rate)
				self.frame_count = 0
 
	def read(self):
		# return the frame most recently read
		return self.frame
 
	def stop(self):
		# indicate that the thread should be stopped
		self.stopped = True

