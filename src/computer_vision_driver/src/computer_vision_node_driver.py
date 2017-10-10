#!/usr/bin/python2
import rospy
import signal
import sys
from computer_vision_driver.msg import CvInfo

def signal_handler(signal, frame):
    print ""
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)

    rospy.init_node("computer_vision_node_driver")
    cv_info_publisher = rospy.Publisher("cv_info_topic", CvInfo)
    cvinfo_msg = CvInfo()
    reset_cvinfo_msg(cvinfo_msg) 

    cam_number = raw_input("Please enter the camera number: ")
    task_number = raw_input("Please enter the task number: ")
    while(not rospy.is_shutdown()):
        try:
            cvinfo_msg.cameraNumber = int(cam_number)
            cvinfo_msg.taskNumber = int(task_number)
            cv_info_publisher.publish(cvinfo_msg)

            print "Message published to cv_info_topic!"
        except ValueError:
            cvinfo_msg.cameraNumber = None
            print "Invalid entry.."


        reset_cvinfo_msg(cvinfo_msg) 
        cam_number = raw_input("Please enter the camera number: ")
        task_number = raw_input("Please enter the task number: ")
        
def reset_cvinfo_msg(p_cvinfo_msg):
    p_cvinfo_msg.cameraNumber = -1
    p_cvinfo_msg.taskNumber = -1
    p_cvinfo_msg.givenColor = -1
    p_cvinfo_msg.givenShape = -1
    p_cvinfo_msg.givenLength = -1
    p_cvinfo_msg.givenDistance = -1

if __name__ == "__main__":
    main()
