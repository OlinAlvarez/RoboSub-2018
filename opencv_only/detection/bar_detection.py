#!/usr/bin/env python2

from utils.color_manager import OpenCVColor
import utils.opencv_tools as OpenCVTools
import numpy as np
import cv2
from enum import IntEnum
from utils.image_metadata import ImageMetaData

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

    # Public Methods
    def detectBar(self, img_metadata):
        """
        Parameters
            opencv_img ImageMetaData

        Returns
            DetectionResult object
        """
        # Make sure data is reloaded before detection. 
        # Reasoning: We do not want to keep creating objects.
        self.detection_result.clear()

        _, contours, _ = self._findContours(img_metadata.getOpenCVImg())

        # If we do not have any contours, we did not detect what we wanted
        if(len(contours) == 0):
            self.detection_result = DetectionResultEnum.NotFound
            return

        largest_area_cnt_val = None 
        largest_cnt = None 
        
        result_obj = self.detection_result
        for cnt in contours:
            cnt_area = cv2.contourArea(cnt)
            
            if(not self._isContourLeadingBar(cnt, cnt_area, img_metadata)):
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

            images_center_x = img_metadata.getWidth() / 2
            images_center_y = img_metadata.getHeight() / 2
            image_origin_tuple = (images_center_x, images_center_y)

            result_obj.obj_center_offset_tuple = OpenCVTools.getObjectsCenterOffset(result_obj.obj_center_tuple, image_origin_tuple)

        return result_obj

    # Private methods
    def _findContours(self, opencv_img):
        """
        Method to encapsulate image processing for contour finding
        """
        # Smoothen out image but keep sharp edges
        blur_options = self.detection_options.blur
        img_blurred = cv2.bilateralFilter(opencv_img, blur_options.pixel_neighborhood_diameter, blur_options.sigma_color_space, blur_options.sigma_coordinate_space)

        # Convert bgr image to hsv 
        img_hsv = cv2.cvtColor(img_blurred, cv2.COLOR_BGR2HSV)

        # Obtain color we want to filter on
        color_filter = self.detection_options.color_filter
        target_color_obj = OpenCVColor(color_filter.r, color_filter.g, color_filter.b)
        target_color_obj.set_rgb([color_filter.r, color_filter.g, color_filter.b])
        lower_bar_hsv = np.array(target_color_obj.get_hsv_lower_bound(color_filter.hue_offset))
        upper_bar_hsv = np.array(target_color_obj.get_hsv_upper_bound(color_filter.hue_offset))

        # Create mask and filter out what we want
        img_mask = cv2.inRange(img_hsv, lower_bar_hsv, upper_bar_hsv)
        img_color_filtered = cv2.bitwise_and(img_blurred, img_blurred, mask=img_mask)

        # Obtain contours
        contour_options = self.detection_options.contour
        img_gray = cv2.cvtColor(img_color_filtered, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Testing", img_gray)

        # We only care about the contours found
        return cv2.findContours(img_gray, contour_options.retrieval_mode, contour_options.approximation_method)

    def _isContourLeadingBar(self, cv_contour, cv_contour_area, img_metadata):
        if(len(cv_contour) > 50):
            return False

        peri = cv2.arcLength(cv_contour, True)
        approx = cv2.approxPolyDP(cv_contour, 0.03 * peri, True)

        # We only want rectangular shapes
        vertices_bound_option = self.detection_options.vertices_bound
        vertices_count = len(approx)
        if(not(vertices_count >= vertices_bound_option.lower_bound and vertices_count <= vertices_bound_option.upper_bound)):
            # if(DEBUG):
                # print "Upper vertices bound: {0} - Lower vertcies bound: {1} - Found vertices count: {2}".format(upper_vertices_count, lower_vertices_count, str(vertices_count))
            return False

        # Ensure contour area is within specified threshold
        calculated_max_area = self.detection_options.max_object_area_percent * img_metadata.getArea()
        calculated_min_area = self.detection_options.min_object_area_percent * img_metadata.getArea()
        if(cv_contour_area > calculated_max_area or cv_contour_area < calculated_min_area):
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
        
        self.max_object_area_percent = .8
        self.min_object_area_percent = .0002

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
        self.retrieval_mode = cv2.RETR_EXTERNAL
        self.approximation_method = cv2.CHAIN_APPROX_SIMPLE

class GenericBoundOptions(object):
    def __init__(self):
        self.lower_bound = None
        self.upper_bound = None
