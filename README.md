# RoboSub Code Repository

# Environment Settings
- Ubuntu 17
- Ros Lunar
- OpenCV2 with python2

# Installation
Followed this link to perform installation for ROS
- http://wiki.ros.org/lunar/Installation/Ubuntu

Used to install opencv2
- http://docs.opencv.org/master/d7/d9f/tutorial_linux_install.htm

# Troubleshoot Problems
- If you are obtaining issues with importing a newly created custom message within ROS, make sure the package name is different from the script being executed.
    - Example: 
        - Package name: computer_vision
        - Ros Node: computer_vision.py

        - Results in an error where computer_vision does not contain msg attribute.

## Adding python package
Add setup.py(ensure that you add dependent packages), uncomment catkin_python_setup(), and add __init__.py to root of package

# What is opencv_only?
- The purpose of this folder is for the early development of the Robosub(October 2017). Once we can confidently detect the objects we can move the code into ROS, our main system. 
