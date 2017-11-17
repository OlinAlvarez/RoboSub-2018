#!/usr/bin/env python2

from utils.color_manager import OpenCVColor
import utils.opencv_tools as OpenCVTools
import numpy as np
import cv2
from enum import IntEnum

"""
Can probably be pulled out later
"""
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
        self._img_height, self._img_width, self._img_color_channel = np.shape(opencv_img)
        self._img_area = self._img_height * self._img_width

    def _canWeCalculate(self):
        if(self.opencv_img is None):
            raise ValueError("opencv_img is None. Cannot calculate anything.")

    def _setDefaultMetaDataValues(self):
        self._img_width = None
        self._img_height = None
        self._img_area = None
        self._img_color_channel = None


class DetectionResult(object):
    def __init__(self):
        """
        Class Data
            obj_detected_bool           Boolean

            obj_contour                 OpenCV Contour

            obj_contour_area            Double

            obj_center_tuple            (x, y) 
                                        Detected objects center

            obj_center_offset_tuple     (x_offset, y_offset)
                                        Offset from image's center. Left/Down is negative. Right/Up is positive

        """
        self.obj_detected_bool = False
        self.obj_contour = None
        self.obj_contour_area = None
        self.obj_center_tuple = (None, None)
        self.obj_center_offset_tuple = (None, None)

    def clear(self):
        self.obj_detected_bool = False
        self.obj_contour = None
        self.obj_contour_area = None
        self.obj_center_tuple = (None, None)
        self.obj_center_offset_tuple = (None, None)

"""
Class will attempt to detect a bar within an image, and give the distance of x and y away from the images center.
"""
class BarDetection(object):
    def __init__(self, bar_detection_options):
        self.detection_options = bar_detection_options
        self.detection_result = DetectionResult()

        # Cache latest image's metadata so it does not require extra computation
        self.img_cached_metadata = ImageMetaData()

    # Public Methods
    def detectBar(self, opencv_img):
        """
        Parameters
            opencv_img OpenCV image object

        Returns
            DetectionResult object
        """
        # Make sure data is reloaded before detection. 
        # Reasoning: We do not want to keep creating objects.
        self.img_cached_metadata.setOpenCVImg(opencv_img)
        self.detection_result.clear()

        _, contours, _ = self._findContours(opencv_img)

        # If we do not have any contours, we did not detect what we wanted
        if(len(contours) == 0):
            self.detection_result = DetectionResultEnum.NotFound
            return

        largest_area_cnt_val = None 
        largest_cnt = None 
        
        result_obj = self.detection_result
        for cnt in contours:
            area_cnt_val = cv2.contourArea(cnt)
            
            if(not self._isContourLeadingBar(cnt, cnt_area)):
                continue

            result_obj.obj_detected_bool = True
            
            # Store largest contour and area
            if(largest_area_cnt_val is None):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt
            elif(cnt_area > largest_area_cnt_val):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt

        if(result_obj.obj_detected_bool):
            result_obj.obj_contour = largest_cnt
            result_obj.obj_area = largest_area_cnt_val
            result_obj.obj_center_tuple = OpenCVTools.getObjectsCenter(largest_cnt)

            images_center_x = self.img_cached_metadata.getWidth() / 2
            images_center_y = self.img_cached_metadata.getHeight() / 2
            image_origin_tuple = (images_center_x, images_center_y)

            result_obj.obj_center_offset_tuple = OpenCVTools.getObjectsCenterOffset(result_obj.obj_center_tuple, image_origin_tuple)

        return result_obj

    # Private methods
    def _findContours(self, opencv_img):
        """
        Method to encapsulate image processing for contour finding
        """
        # Smoothen out image but keep sharp edges
        blur_options = self.detection_options.blur_options
        img_blurred = cv2.bilateralFilter(opencv_img, blur_options.pixel_neighborhood_diameter, blur_options.sigma_color_space, blur_options.sigma_coordinate_space)

        # Convert bgr image to hsv 
        img_hsv = cv2.cvtColor(img_blurred, cv2.COLOR_BGR2HSV)

        # Obtain color we want to filter on
        color_filter = self.detection_options.color_filter
        target_color_obj.set_rgb([color_filter.r, color_filter.g, color_filter.b])
        lower_bar_hsv = np.array(target_color_obj.get_hsv_lower_bound(color_filter.hue_offset))
        upper_bar_hsv = np.array(target_color_obj.get_hsv_upper_bound(color_filter.hue_offset))

        # Create mask and filter out what we want
        img_mask = cv2.inRange(img_hsv, lower_bar_hsv, upper_bar_hsv)
        img_color_filtered = cv2.bitwise_and(img_blurred, img_blurred, mask = img_mask)

        # Obtain contours
        contour_options = self.detection_options.contour
        img_gray = cv2.cvtColor(img_color_filtered, cv2.COLOR_BGR2GRAY)

        # We only care about the contours found
        return cv2.findContours(img_gray, contour_options.retrieval_mode, contour_options.approximation_method)

    def _isContourLeadingBar(self, cv_contour, cv_contour_area):
        if(len(cv_contour) > 50):
            return False

        peri = cv2.arcLength(cv_contour, True)
        approx = cv2.approxPolyDP(cv_contour, 0.03 * peri, True)

        # We only want rectangular shapes
        vertices_bound_option = self.detection_options.vertices_bound
        vertices_count = len(approx)
        if(not(vertices_count >= vertices_bound_option.lower and vertices_count <= vertices_bound_option.upper)):
            # if(DEBUG):
                # print "Upper vertices bound: {0} - Lower vertcies bound: {1} - Found vertices count: {2}".format(upper_vertices_count, lower_vertices_count, str(vertices_count))
            return False

        # Ensure contour area is within specified threshold
        if(area_cnt_val > max_object_area_threshold or area_cnt_val < min_object_area_threshold):
            return False
            # if(DEBUG):
                # print "area_cnt_val {0} - max_area {1} - min_area{2}".format(area_cnt_val, max_object_area_threshold, min_object_area_threshold)


        # if(DEBUG):
            # rect = cv2.minAreaRect(cnt)
            # box = cv2.boxPoints(rect)
            # box = np.int0(box)
            # img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

            # #Write the amount of contours found on the detected object
            # M = cv2.moments(cnt)
            # if(M['m00'] != 0):
                # cx = int(M['m10']/M['m00'])
                # cy = int(M['m01']/M['m00'])
                # img_result = cv2.putText(img_result, str(len(cnt)), (cx,cy), cv2.FONT_HERSHEY_PLAIN, 2, 255)
        return True

"""
Created to allow for tweaking of options.
There will be hardcoded values that worked for demo sample.
"""
class BarDetectionOptions(object):
    def __init__(self):
        self.color_filter = ColorFilterOption()
        self.blur = BlurOption()
        self.contour = ContourOption()
        
        self.vertices_bound = GenericBoundOptions()
        self.vertices_bound.lower_bound = 4
        self.vertices_bound.upper_bound = 8
        
        self.max_object_area = .8
        self.min_object_area = .0002

    class ColorFilterOption(object):
        def __init__(self):
            self.r = 235
            self.g = 254
            self.b = 180
            self.hue_offset = 15

    class BlurOption(object):
        def __init__(self):
            self.pixel_neighborhood_diameter = 9
            self.sigma_color_space = 65
            self.sigma_coordinate_space = 75

    class ContourOption(object):
        def __init__(self):
            self.retrieval_mode = cv2.CV_RETR_EXTERNAL
            self.approximation_method = cv2.CV_CHAIN_APPROX_SIMPLE

    class GenericBoundOptions(object):
        def __init__(self):
            self.lower_bound = None
            self.upper_bound = None

