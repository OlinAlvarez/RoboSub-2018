#!/usr/bin/env python2
import numpy as np


class ImageMetaData(object):
    """
    Purpose is to hold an opencv image's metadata with lazy loading.
    Do not calculate metadata unless we have to.
    """
    def __init__(self):
        """
        Parameter
            opencv_img      Object
            _img_width      Double
            _img_height     Double
            _img_area       Double
        """
        self.opencv_img = None
        self._img_width = None
        self._img_height = None
        self._img_area = None

        # Not sure what this is right now..
        self._img_color_channel = None

    # Public Method
    def setOpenCVImg(self, opencv_img):
        self.opencv_img = opencv_img
        self._setDefaultMetaDataValues()

    def getOpenCVImg(self):
        return self.opencv_img

    def getWidth(self):
        self._canWeCalculate()

        if(self._img_width is None):
            self.calculateImgShape()

        return self._img_width

    def getHeight(self):
        self._canWeCalculate()

        if(self._img_height is None):
            self.calculateImgShape()

        return self._img_height

    def getArea(self):
        self._canWeCalculate()
        
        if(self._img_area is None):
            self._img_area = self.getWidth() * self.getHeight()

        return self._img_area

    # Helper method
    def calculateImgShape(self):
        self._canWeCalculate()
        self._img_height, self._img_width, self._img_color_channel = np.shape(self.opencv_img)
        self._img_area = self._img_height * self._img_width

    def _canWeCalculate(self):
        if(self.opencv_img is None):
            raise ValueError("opencv_img is None. Cannot calculate anything.")

    def _setDefaultMetaDataValues(self):
        self._img_width = None
        self._img_height = None
        self._img_area = None
        self._img_color_channel = None


