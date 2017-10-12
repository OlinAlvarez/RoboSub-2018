#!/usr/bin/env python2

from base_task import BaseTask
import base_task
from hardware.camera import Camera

"""
Does not require input data to execute.
"""
class TakePictureTask(BaseTask):
    def __init__(self, obj_camera):
        """
        Parameters
            obj_camera Camera
        """
        super(self.__class__, self).__init__("Take Picture")

        if(not isinstance(obj_camera, Camera)):
            raise Exception("TakePictureTask requires a camera object")

        self._camera = obj_camera

    def initialize(self):
        super(self.__class__, self).initialize()
        self._camera.set_on()

        if(not self._camera.is_on()):
            raise base_task.InitializationException("Camera is not ready. Please make sure camera is on")

        return

    def execute(self):
        super(self.__class__, self).execute()
        self._input_data = self._camera.capture_image()

    def handle_results(self):
        super(self.__class__, self).handle_results()

        # Store the output tuple for task chaining
        self._output_data = self._input_data
