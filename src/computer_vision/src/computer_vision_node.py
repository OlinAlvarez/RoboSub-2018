#!/usr/bin/python2
import rospy
import cv2

from computer_vision.msg import FrontCamDistance
from computer_vision_driver.msg import CvInfo

from hardware.camera import Camera
from hardware.camera import CameraLocation

def main():

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

        cam_number = cv_info_msg.CameraNumber

        # Guaranteed to have a message.
        if  (cam_number == CameraLocation.FRONT) and \
            (not available_cameras[cam_number].is_camera_on):

            print "Front camera about to do work"

        elif(cam_number == CameraLocation.UNKNOWN):

            print "Cameras are about to be turned off"

        loop_rate.sleep()
    
def default_cam_msg_data(oCamDistanceMsg):
    if(isinstance(oCamDistanceMsg, FrontCamDistance)):
        oCamDistanceMsg.FrontCamForwardDistance = None
        oCamDistanceMsg.FrontCamHorizontalDistance = None
        oCamDistanceMsg.FrontCamVerticalDistance = None
    
    return

if __name__ == "__main__":
    init_globals()
    main()
