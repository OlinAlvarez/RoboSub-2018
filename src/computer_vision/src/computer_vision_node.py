#!/usr/bin/python2
import rospy
import cv2

from computer_vision.msg import FrontCamDistance
from computer_vision_driver.msg import CvInfo

from hardware.camera import Camera
from hardware.camera import CameraLocation
from hardware.camera_manager import CameraManager

from objectives.objective_factory import ObjectiveFactory, ObjectiveEnum
from objectives.base_objective import ObjectiveStatusEnum

def main():
    rospy.init_node("computer_vision_node")

    fcd_pub = rospy.Publisher("front_cam_distance", FrontCamDistance)
    fcd_msg = FrontCamDistance()

    # Computer Vision Hardware
    camera_manager = CameraManager.get_instance() 

    # Loop 100 times per second
    loop_rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        default_cam_msg_data(fcd_msg)

        # Wait for one message from cv_info_topic
        cv_info_msg = rospy.wait_for_message("cv_info_topic", CvInfo)

        camera_location = CameraLocation(cv_info_msg.cameraNumber)
        objective_enum = ObjectiveEnum(cv_info_msg.taskNumber)
        
        # Nothing to do if unknown camera
        if (not camera_manager.contains_camera(camera_location) and camera_location != CameraLocation.ALL_OFF):
            print "Unknown camera number '" + str(camera_location) + "'"
            continue

        # Turn off all cameras if instructed to do so.
        if (camera_location == CameraLocation.ALL_OFF):
            camera_manager.turn_off_all_cameras()
            print "Turning off all cameras"
            continue


        # We have a camera to turn on and start working with.
        primary_cam_obj = camera_manager.get_camera(camera_location)
        if(primary_cam_obj.set_on()):
            print "Camera at location '{0}' is turning on".format(camera_location.name)
        else:
            print "Camera at location '{0}' is already on".format(camera_location.name)

        # Perform camera functionality
        objective_to_run = ObjectiveFactory.create_objective(objective_enum, camera_manager)
        objective_to_run.start_objective()
        if(ObjectiveStatusEnum.SUCCESS == objective_to_run.get_status()):
            print "Objective '{0}' succeeded!!! :)".format(objective_to_run.get_name())
        else:
            print "Objective '{0}' failed... :(".format(objective_to_run.get_name())

        loop_rate.sleep()
    
def default_cam_msg_data(oCamDistanceMsg):
    if(isinstance(oCamDistanceMsg, FrontCamDistance)):
        oCamDistanceMsg.frontCamForwardDistance = -1
        oCamDistanceMsg.frontCamHorizontalDistance = -1
        oCamDistanceMsg.frontCamVerticalDistance = -1
    
    return

if __name__ == "__main__":
    main()
