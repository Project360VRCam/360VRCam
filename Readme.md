# User Manual
#### Recording
To use the camera software you need to connect to the Raspberry Pi that controls the camera, we call this the MasterPi. You can connect to the MasterPi using ssh:

```
ssh pi@masterpiaddress
```
The default user is pi, and the password is raspberry.

Start the program [masterpi.py](https://github.com/Project360VRCam/360VRCam/blob/master/masterpi.py):
```
python masterpi.py
```
and wait for the leds on all Raspberries to light up. The led indicates that the Raspberry is ready.

The MasterPi should now ask what you want to do:
```
Do you want to: 1.Take picture 2.Start recording or 3.Stop recording: 
```
The camera is now ready, you can start taking pictures or record video.

Pictures and videos are saved in the format *pictureN_C.png* or *videoN_C.avi* where N is an incrementing number for each picture/video taken and C is the number of the camera used for that picture/video.


#### Stitching



