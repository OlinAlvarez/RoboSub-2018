#!/usr/bin/python2
import rospy
import cv2

from computer_vision.msg import FrontCamDistance
from computer_vision_driver.msg import CvInfo

from hardware.camera import Camera
from hardware.camera import CameraLocation

def main():
    rospy.init_node("computer_vision_node")

    fcd_pub = rospy.Publisher("front_cam_distance", FrontCamDistance)
    fcd_msg = FrontCamDistance()

    # Computer Vision Hardware
    available_cameras = dict()
    available_cameras[CameraLocation.FRONT] = Camera(CameraLocation.FRONT)

    # Loop 100 times per second
    loop_rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        default_cam_msg_data(fcd_msg)

        # Wait for one message from cv_info_topic
        cv_info_msg = rospy.wait_for_message("cv_info_topic", CvInfo)

        cam_number = cv_info_msg.cameraNumber

        print (cam_number == CameraLocation.FRONT)
        # Guaranteed to have a message.
        if  (cam_number == CameraLocation.FRONT):
            if (not available_cameras[cam_number].is_camera_on()):
                print "Front camera about to do work"
                available_cameras[cam_number].camera_on()
            else:
                print "Front camera already doign work!!"

        elif(cam_number == CameraLocation.ALL_OFF):

            print "Cameras are about to be turned off"

            for k,v in available_cameras.items():
                v.camera_off()
        else:

            print "Unknown camera number supplied '" + str(cam_number) + "'"

        loop_rate.sleep()
    
def default_cam_msg_data(oCamDistanceMsg):
    if(isinstance(oCamDistanceMsg, FrontCamDistance)):
        oCamDistanceMsg.frontCamForwardDistance = -1
        oCamDistanceMsg.frontCamHorizontalDistance = -1
        oCamDistanceMsg.frontCamVerticalDistance = -1
    
    return

if __name__ == "__main__":
    main()
