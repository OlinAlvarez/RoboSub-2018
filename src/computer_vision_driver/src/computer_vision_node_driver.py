#!/usr/bin/python2
import rospy
from computer_vision_driver.msg import CvInfo

def main():
    rospy.Publisher("cv_info_topic", CvInfo)
    print "Hello world" 

if __name__ == "__main__":
    main()
