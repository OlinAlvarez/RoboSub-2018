#!/usr/bin/python2
from enum import IntEnum
import cv2
import os.path
import os
import datetime

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

    def capture_image(self):
        """
        Takes picture using opencv

        Returns
            (boolean, image)
        """
        if(not self.is_on):
            raise Exception("Please turn camera on before using it.")

        return self._cv2_vid_capture.read()

    def capture_and_save_image(self, file_name_location = None):
        """
        Captures image and saves image to the specified location
        If not location is provided, image will be saved to '~/Pictures/img_...'

        Returns
            Image if successful
            None if not
        """

        successful_img, image = self.capture_image()

        if(not successful_img):
            return None

        if(file_name_location is None):
            dt_now = datetime.datetime.today()
            dt_suffix = dt_now.strftime("%x_%X").replace("/","").replace(":","")

            full_path = os.path.expanduser("~/Pictures")
            if(not os.path.isdir(full_path)):
                os.mkdir(full_path)

            full_path = full_path + "/robosub_temp"
            if(not os.path.isdir(full_path)):
                os.mkdir(full_path)
            file_name_location = full_path + "/" + "ros_temp_img_{0}.png".format(dt_suffix)

        cv2.imwrite(file_name_location, image)

        return None

    def set_on(self):
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

    def set_off(self):
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

    def get_location(self):
        return self._camera_location

    def get_dev_index(self):
        return self._video_dev_index

    def is_on(self):
        return self._is_on == True
