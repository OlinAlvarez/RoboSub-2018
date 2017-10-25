#!/usr/bin/env python2
from camera import Camera
from camera import CameraLocation

class CameraManager:
    _CameraManager = None

    @staticmethod
    def get_instance():
        if(CameraManager._CameraManager is not None):
            return CameraManager._CameraManager

        CameraManager._CameraManager = CameraManager() 
        return CameraManager._CameraManager

    def __init__(self):
        self._available_cameras = dict()
        self.initialization()

    def initialization(self):
        # Delete existing camera
        self._available_cameras.clear()

        # Init cameras
        self._available_cameras[CameraLocation.FRONT] = Camera(CameraLocation.FRONT, 0)
        self._available_cameras[CameraLocation.BOTTOM] = Camera(CameraLocation.BOTTOM, 1)

    def contains_camera(self, enum_cam_location):
        """
        Parameters
            enum_cam_location CameraLocation 

        Returns
            Boolean representing if camera exists
        """
        return self._available_cameras.has_key(enum_cam_location)

    def get_camera(self, enum_cam_location):
        """
        Parameters
            enum_cam_location CameraLocation 

        Returns
            Camera object else None
        """
        if(self.contains_camera(enum_cam_location)):
            return self._available_cameras[enum_cam_location]

        return None

    def add_new_camera(self, enum_cam_location, obj_camera):
        """
        Parameters
            obj_camera Camera

        Returns
            True if succesfully added
            False if camera already exists
        """
        if(self.contains_camera(obj_camera)):
            return False

        self._available_cameras[enum_cam_location] = obj_camera
        return True

    def delete_camera(self, enum_camera_location):
        """
        Parameters
            enum_cam_location CameraLocation 

        Returns
            Boolean explaining if camera was removed
        """
        return (self._available_cameras.pop(enum_camera_location, None) is not None)

    def turn_off_all_cameras(self):
        for enum_cam_loc, cam in self._available_cameras.items():
            cam.set_off()

        return
