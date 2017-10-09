#!/usr/bin/python2
from enum import IntEnum
import cv2

class CameraLocation(IntEnum):
    ALL_OFF = 0
    FRONT = 1
    BOTTOM = 2
    UNKNOWN = -1

class Camera:
    def __init__(self, cam_location, video_index):
        """
        Params:
            cam_location CameraLocation
            video_index  /dev/video* index
        """
        self._camera_location = cam_location
        self._is_on = False 
        self._video_dev_index = video_index
        self._cv2_vid_capture = None

    def camera_on(self):
        """
        Turns on camera and initializes opencv capture feed

        Returns
            True    if first time turning on
            False   if already on or error occurred
        """
        if(self._cv2_vid_capture is not None):
            return False

        self._cv2_vid_capture = cv2.VideoCapture(self._video_dev_index)

        if(not self._cv2_vid_capture.isOpened()):
            raise Exception("Cannot open video at index '{0}'".format(self._video_dev_index))

        self._is_on = True
        return True

    def camera_off(self):
        """
        Turns off camera and releases opencv2 resources

        Returns
            True    if camera is turned off
            False   if camera is already off
        """
        if(self._is_on and self._cv2_vid_capture is not None):
            self._cv2_vid_capture.release()
            self._cv2_vid_capture = None
            self._is_on = False
            return True

        return False

    def toggle_camera(self):
        if(self._is_on):
            return self.camera_off()

        return self.camera_on()

    def get_camera_location(self):
        return self._camera_location

    def get_camera_dev_index(self):
        return self._video_dev_index

    def is_camera_on(self):
        return self._is_on == True

