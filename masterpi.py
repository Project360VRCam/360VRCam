"""Master program: 1 raspberry pi as acess point, running web server probably implemented with NodeJS? nginx? apache?, cameras connected

Scenario 1: Take picture
1. Get a signal from the web api when someone presses the button "Take picture"
2. Send a "1" on a GPIO-pin to all the slaves so that every camera takes a picture.
3. Take a picture itself 

Scenario 2: Start recording video
1. Get a signal from the web api when user presses the button "Start recording"
2. Send a "1" on another GPIO-pin to all the slaves 
3. Start recording itself --> Run picture program code
"""

import os
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)

while True:
    status = raw_input("Do you want to: 1.Take picture 2.Start recording or 3.Stop recording: ")
    #Take a picture
    if status=='1':
        GPIO.output(18,True)
        os.system("python record.py -n 1")
        time.sleep(0.05)
        GPIO.output(18,False)
        print "A picture was taken."
    #Start recording
    elif status=='2':
        GPIO.output(17,True)
        print "Started recording..."
        os.system("python record.py -n 1")
    #Stop recording    
    elif status=='3':
        GPIO.output(17,False)
        print "Stopped recording."   
    else:
        print "Error: Wrong input"