#!/usr/bin/env python2

from base_task import BaseTask, InitializationException, ExecutionException, HandleResultsExceptions

import cv2
"""
Mainly used as the task test driver

I would like to take a picture using opencv2 and saving it to ~/Pictures/robosub_tmp folder
"""

class TakeOpenCVPicture(BaseTask):
    def __init__(self, obj_opencv_camera):
        """
        Parameters
            obj_opencv_camera Camera object
        """
        super(TakeOpenCVPicture, self).__init__()
        self._task_name = "OpenCV Take Picture And Save"
        self._opencv_cam = obj_opencv_camera
        self._result_img = None
        self._ret_val = None

    def initialize(self):
        super(TakeOpenCVPicture, self).initialize()
        print "initialize called"

        # Check if camera is still on.
        if(not self._opencv_cam.is_on()):
            raise InitializationException("Camera is not ready to be used. Please make sure OpenCV was able to initialize VideoCapture on hardware")

    def execute(self):
        super(TakeOpenCVPicture, self).execute()
        print "execute called"
        print "Taking a picture using {0} camera".format(str(self._opencv_cam.get_location()))
        self._opencv_cam.capture_and_save_image()
        
    def handle_results(self):
        super(TakeOpenCVPicture, self).handle_results()
        print "handle_results called"
