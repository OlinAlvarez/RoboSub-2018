#!/usr/bin/python3
import rospy
from computer_vision.msg import FrontCamDistance

def main():
    front_cam = FrontCamDistance()

    front_cam.frontCamForwardDistance = 999
    front_cam.frontCamHorizontalDistance = 999
    front_cam.frontCamVerticalDistance = 999
    print(front_cam)

if __name__ == "__main__":
    main()
