import jetson.inference 
import jetson.utils

from jetson.inference import detectNet
from jetson.utils import loadImage, saveImage

net = detectNet("ssd-mobilenet-v2", threshold=0.5)

#camera = videoSource("/dev/video0") # '/dev/video0' for V4L2
image = loadImage("image.jpg")
detections = net.Detect(image)
#detection = detections[0]

if len(detections) > 0:

       detection = detections[0]

print(detection)

#display = videoOutput("display://0") # 'my_video.mp4' for file
#while display.IsStreaming(): # main loop will go here

#display = videoOutput("display://0") # 'my_video.mp4' for file
#while display.IsStreaming(): # main loop will go here
#img = camera.Capture()
#if img is None: # capture timeout
#continue


#image.Render(image)
#image.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))

#if len(detections) >=0:
    #detection = detections[0]
    #class_id = detection.ClassID
    #confidence = detection.Confidence
    #left,top,right,bottom = detection.Left, detection.Top, detection.Right, detection.Bottom #Bounding box connrdinates

saveImage("detresult.jpg", image)
