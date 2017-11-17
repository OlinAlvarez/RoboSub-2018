#!/usr/bin/env python2

from base_task import BaseTask, InitializationException, ExecutionException, HandleResultsExceptions

import cv2
from hardware.camera import CameraLocation
"""
Mainly used as the task test driver

I would like to take a picture using opencv2 and saving it to ~/Pictures/robosub_tmp folder
"""

class TakeOpenCVPicture(BaseTask):
    def __init__(self, topic_msg, camera_manager_obj):
        """
        Parameters
            obj_opencv_camera Camera object
        """
        super(self.__class__, self).__init__()
        self._task_name = "OpenCV Take Picture And Save"
        self._camera_manager = camera_manager_obj
        self._camera = None
        self._result_img = None
        self._ret_val = None

    def initialize(self):
        super(self.__class__, self).initialize()
        print "initialize called"

        self._camera = self._camera_manager.get_camera(CameraLocation.FRONT)

        # Check if camera is still on.
        if(self._camera is None or not self._camera.is_on()):
            raise InitializationException("Camera is not ready to be used. Please make sure OpenCV was able to initialize VideoCapture on hardware")

    def execute(self):
        super(self.__class__, self).execute()
        print "execute called"
        print "Taking a picture using {0} camera".format(str(self._camera.get_location()))
        self._camera.capture_and_save_image()
        
    def handle_results(self):
        super(self.__class__, self).handle_results()
        print "handle_results called"
