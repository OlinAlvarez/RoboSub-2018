#!/usr/bin/python2
import rospy
from computer_vision_driver.msg import CvInfo

def main():
    cv_info_publisher = rospy.Publisher("cv_info_topic", CvInfo)
    cvinfo_msg = CvInfo()
    reset_cvinfo_msg(cvinfo_msg) 

    answer = raw_input("Please enter the camera number['q' to exit]:")
    while(answer != "q" or not rospy.is_shutdown()):
        try:
            cvinfo_msg.cameraNumber = int(answer)
            cv_info_publisher.publish(cvinfo_msg)

            print "Message published to cv_info_topic!"
        except ValueError:
            cvinfo_msg.cameraNumber = None
            print "Invalid entry.."


        reset_cvinfo_msg(cvinfo_msg) 
        answer = raw_input("Please enter the camera number['quit' to exit]:")
        
def reset_cvinfo_msg(p_cvinfo_msg):
    p_cvinfo_msg.cameraNumber = None
    p_cvinfo_msg.taskNumber = None
    p_cvinfo_msg.givenColor = None
    p_cvinfo_msg.givenShape = None
    p_cvinfo_msg.givenLength = None
    p_cvinfo_msg.givenDistance = None

if __name__ == "__main__":
    main()
