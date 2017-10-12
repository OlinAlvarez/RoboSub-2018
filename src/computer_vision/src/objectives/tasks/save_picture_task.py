#!/usr/bin/env python2

from base_task import BaseTask
import base_task
import os.path
import os
import datetime
import cv2

"""
Expects an opencv tuple (boolean, image)
"""
class SavePictureTask(BaseTask):
    def __init__(self, absolute_save_path_string = None):
        super(self.__class__, self).__init__("Save Picture")
        self._absolute_save_path = absolute_save_path_string

    def initialize(self):
        super(self.__class__, self).initialize()
        if(self._input_data is None or not isinstance(self._input_data, tuple)):
            raise base_task.InitializationException("Requires a (boolean, image) from opencv")
        return

    def execute(self):
        super(self.__class__, self).execute()
        successful_img, image = self._input_data
        if(not successful_img):
            raise base_task.ExecutionException("Image could not be saved")

        if(self._absolute_save_path is None):
            dt_now = datetime.datetime.today()
            dt_suffix = dt_now.strftime("%x_%X").replace("/","").replace(":","")

            full_path = os.path.expanduser("~/Pictures")
            if(not os.path.isdir(full_path)):
                os.mkdir(full_path)

            full_path = full_path + "/robosub_temp"
            if(not os.path.isdir(full_path)):
                os.mkdir(full_path)
            self._absolute_save_path = full_path + "/" + "ros_temp_img_{0}.png".format(dt_suffix)

        cv2.imwrite(self._absolute_save_path, image)


    def handle_results(self):
        super(self.__class__, self).handle_results()

        # Set output data back to tuple incase we need to continue chaining after save.
        self._output_data = self._input_data

