#!/usr/bin/env python2
import cv2
import numpy as np

class OpenCVColor(object):
    def __init__(self, r_val, g_val, b_val):
        self.r = r_val
        self.g = g_val
        self.b = b_val

        # Cache hsv so we do not waste resources
        self._cached_hsv = None

    def set_red(self, r_val):
        self._check_valid_color(r_val)

        self.r = r_val
        self._cached_hsv = None

    def set_green(self, g_val):
        self._check_valid_color(g_val)

        self.g = g_val
        self._cached_hsv = None

    def set_blue(self, b_val):
        self._check_valid_color(b_val)

        self.b = b_val
        self._cached_hsv = None

    def get_red(self):
        return self.r

    def get_green(self):
        return self.g

    def get_blue(self):
        return self.b

    def set_rgb(self, rgb_list):
        if(not isinstance(rgb_list, list)):
            raise TypeError("rgb_list needs to be a list")

        if(len(rgb_list) != 3):
            raise ValueError("rgb_list can only take 3 values. [r, g, b]")

        for color_index in range(3):
            color_val = rgb_list[color_index]
            
            if(color_index == 0):
                self.set_red(color_val)
            elif(color_index == 1):
                self.set_green(color_val)
            else:
                self.set_blue(color_val)
    
    def get_rgb(self):
        return [self.r, self.g, self.b]

    def get_hsv(self):
        if(self._cached_hsv is None):
            self._cached_hsv = cv2.cvtColor(np.uint8([[[self.b, self.g, self.r]]]), cv2.COLOR_BGR2HSV)[0][0]

        return self._cached_hsv

    def get_hsv_lower_bound(self, hue_offset):
        hsv = self.get_hsv()
        hsv_hue = hsv[0]

        # np.uint8 conversion messes up by 1
        if(hue_offset > hsv_hue):
            hue_offset += 1

        return [np.uint8(hsv_hue - hue_offset), 50, 50]

    def get_hsv_upper_bound(self, hue_offset):
        hsv = self.get_hsv()
        hsv_hue = hsv[0]
        if((hue_offset + hsv_hue) > 255):
            hue_offset += 1

        return [np.uint8(hsv_hue + hue_offset), 255, 255]

    def _check_valid_color(self, color_val):
        if(not self.is_valid_color_value(color_val)):
            raise ValueError("'{0}' color value is out of bound.".format(str(color_val)))

    def is_valid_color_value(self, color_val):
        if(color_val > 255 or color_val < 0):
            return False

        return True

