#!/usr/bin/python2
from enum import Enum

class CameraLocation(Enum):
    FRONT = 1
    BACK = 2
    UNKNOWN = 0

class Camera:
    def __init__(self, cam_location):
        """
        Params:
            cam_location CameraLocation
        """
        self._camera_location = cam_location
        self._is_on = False

    def camera_on(self):
        self._is_on = True

    def camera_off(self):
        self._is_on = False

    def toggle_camera(self):
        self._is_on = not self._is_on

    def get_camera_location(self):
        return self._camera_location

    def is_camera_on(self):
        return self._is_on == True
