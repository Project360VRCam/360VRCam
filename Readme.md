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


#Stitching
After trying different stitching software we have come out with following recommendation.
Panorama viewing software (After stitch):
WPanorama (Image viewer)
GoPro VR Player (Video player)
Both of these softwares are freeware. 

We used Image composite editor (Freeware) from Microsoft to stitch the images. The steps are pretty straight forward. We start with simply by loading the images. 

From the application front-screen select the option “New Panorama From Images”. 
Load the pictures you want to stitch together from the “File Open” dialog box. You can select multiple pictures by holding the  “Ctrl” key down whilst clicking on each picture, or you can also drag and drop files onto the application.
Click on Stitch. You now get the first view of your panorama. If you are feeling so inclined you can play with the Projection (top right). If it all goes wrong whilst playing here, just click on “Back” (top-left).
Crop to Size. This is you’re next chance to play. Click on “Auto Crop” (top right) and the software selects the “largest” rectangular image it can from the assembly. After selecting “Auto Crop” check the small tickbox marked “Use auto completion” and you will see the software creatively filling in the rest of your picture. 
The main choice you need to make is the file format. A JPG image will be smaller, but some detail will be lost. If you want a “lossless” format chose to export as a PNG image. Once you are ready with your stitched picture on the Wpanorama.

Alternatively Autopano image stitching can be used as well but it is not free. 

On the other hand video stitching is a bit expensive and complex process. We didn’t find any well performed video stitching software for free. However, there are trial versions. This versions has some limitations but good enough to try.   The only way to master the video stitching skill is to practice with more and more new videos. There are lots of detail to notice in a single video. 

We used Autopano Video Pro plus Autopano Giga to stitch the videos. Alternatively we also tried the VideoStitch studio as well. The limitation of VideoStitch studio is that it is a hardware (NVIDIA graphics card 4GB) dependent  software. 

As we already know the stitching process is a bit complex with Autopano Video Pro , we will describe  the most important steps here. 
Once you launch Autopano Video Pro, the first option you see is to drag and drop your videos into the project. After dropping all of the videos you can see your clips on the preview panel.
The second step is synchronization. There are different types of synchronizations: Motion, Audio. Depending on your clips you can do both sort of synchronization or either one. 
The next step is to stitch your footage. Click on the Stitch tab, and find the camera pre-sets. Select your camera and click the Stitch button. Autopano Video Pro will now run through and stitch all the clips together and output an equirectangular image.
You need to set a default field of view for you viewers when they start up a 360 video. The reason you want the primary action in the center of the screen at the start of a 360 video is because the viewer will be looking all around once the video starts. You want to immediately direct their attention by already having them oriented towards the action. 

The best way to focus your viewer is to move the primary action area to the center of the screen (the direct center of the 360 video is facing forward for the viewer when they start watching). If the point of interest was too far towards the edges, this would force the viewer to 'wander' too much, looking left or right to find the action. Reorienting the 360 video so that the action is in the center of the frame is easy: go to the beginning, then just click and drag on the preview, the same as you do to fix the horizontal line.
At the bottom your clip there are four different timelines. We have the horizon, the stitch, color, and mask and this so we can make adjustments to each one of these independently of the other. When you finish adjusting everything and are happy with your video, go ahead and click Apply.At the top of your video are red and purple bars. The red indicator indicates the render in and out. Purple is the current selection. If you just want to do adjustments on certain sections of the video, you can adjust that with these red and purple indicators. 
Our next step is stabilization and picture correction using the corresponding tabs. After that we fine tune the videos and blend it.  360 video uses multiple videos overlapped to make a composite. There are basically two types of blending to make that overlap: sharp blending and smooth blending.
After all these steps we are ready to final render and export the clip. Before we finish the 360 video you need to do one more step: inject some metadata into your video file so that video players will recognize it as a 360 video.
