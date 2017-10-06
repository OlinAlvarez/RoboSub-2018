import rospy
import cv2
import numpy as np
from std_msgs.msg import String

fcdPub = rospy.Publisher('/front_cam_distance','auv_cal_state_la_2017/FrontCamDistance')
bcdPub = rospy.Publisher('/bottom_cam_distance','auv_cal_state_la_2017/BottomCamDistance')
tiPub = rospy.Publisher('/target_info','auv_cal_state_la_2017/TargetInfo')

fcdMst = String()
bcdMsg = String()
tiMsg  = String()

#fcdMsg = rosmessage('auv_cal_state_la_2017/FrontCamDistance')
#bcdMsg = rosmessage('auv_cal_state_la_2017/BottomCamDistance')
#tiMsg = rosmessage('auv_cal_state_la_2017/TargetInfo')

tiMsgTemp = tiMsg
cvisub = rospy.Subscriber('/cv_info')
## Useful commands
# hostname -I
# rosinit('10.85.43.217')
# rosshutdown
# synclient HorizEdgeScroll=0 HorizTwoFingerScroll=0
# roboticsAddons
# folderpath = '/home/auv/catkin_ws/src'
# rosgenmsg(folderpath)


frontCam = False
bottomCam = False
found = False

#rate of 100hz

rospy.Rate(100)

while 1:
	#default values
    fcdMsg.FrontCamForwardDistance = 999
    fcdMsg.FrontCamHorizontalDistance = 999
    fcdMsg.FrontCamVerticalDistance = 999
    bcdMsg.BottomCamForwardDistance = 999
    bcdMsg.BottomCamHorizontalDistance = 999
    bcdMsg.BottomCamVerticalDistance = 999
    tiMsg.State = 0
    tiMsg.Angle = 0
    tiMsg.Height = 0
    tiMsg.Direction = 0
	
	# receive cviMsg
    # TaskNumber, GivenColor, GivenShape, GivenLength, GivenDistance
    cviMsg = receive(cviSub) 
    
    ## Evaluate inputs
	if cviMsg.CameraNumber == 1 and frontCam == False:
        delete(imaqfind)
        camera = videoinput('linuxvideo',2,'RGB24_744x480')
        #camera = videoinput('linuxvideo',1,'RGB24_1280x720')
        triggerconfig(camera,'manual')     # speeds up image acquisition for videoinput
#         camera.FramesPerTrigger = 1
        start(camera)
        
        #         if ~strcmp(camera.Name,'DFK 22AUC03')
        #             camera = webcam(1)
        #         end
        #camera = webcam(1)
        frontCam = True
        bottomCam = False

    elif cviMsg.CameraNumber == 2 and bottomCam == False:
        delete(imaqfind)
        camera = videoinput('linuxvideo',1,'RGB24_744x480')
        triggerconfig(camera,'manual')
        start(camera)
        frontCam = False
        bottomCam = True
    elif cviMsg.CameraNumber == 0 and (frontCam == True or bottomCam == True):
        stop(camera)
        frontCam = False
        bottomCam = False
        found = False
        #testTimer = 0
        disp("task done")
    end
    
    ## Run camera
    if frontCam
        FrontCamera(cviMsg)
    end
    
    if bottomCam
        BottomCamera(cviMsg)
    end
    
    ## Send Msg
    send(fcdPub, fcdMsg)
    send(bcdPub, bcdMsg)
    send(tiPub, tiMsg)
    
    ## Loop rate (10Hz)
    waitfor(rate)
end
