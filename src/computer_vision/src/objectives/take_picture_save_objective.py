#!/usr/bin/env python2

from tasks.take_picture_task import TakePictureTask
from tasks.save_picture_task import SavePictureTask
from hardware.camera import CameraLocation
from hardware.camera_manager import CameraManager

import cv2
import os
import datetime
from base_objective import BaseObjective
"""
Mainly used as the task test driver

I would like to take a picture using opencv2 and saving it to ~/Pictures/robosub_tmp folder
"""

class TakeOpenCVPictureAndSave(BaseObjective):
    def __init__(self, obj_camera_manager, max_retries = 1):
        """
        Parameters
            obj_opencv_camera Camera object
        """
        super(self.__class__, self).__init__("OpenCV Take Picture And Save", max_objective_retries = max_retries)

        if(not isinstance(obj_camera_manager, CameraManager)):
            raise Exception("TakeOpenCVPictureAndSave is expecting a CameraManager.")

        self._camera_manager = obj_camera_manager
        self.initialize_task_list()

    def initialize_task_list(self):
        """
        Purpose is to create all the necessary tasks that will chain together to accomplish task
        """
        # Take Picture
        self._task_list.append(TakePictureTask(self._camera_manager.get_camera(CameraLocation.FRONT)))

        # Save Picture Task
        self._task_list.append(SavePictureTask())


