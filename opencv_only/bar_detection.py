#!/usr/bin/env python2

import cv2
import numpy as np
import time

# The purpose of this task is to ensure the camera is parallel with a bar.
# This will guide us into the direction of the bouy.

# DEBUG = True
DEBUG = False
def main():
    img_path = "./images/front_cam/fourthrun/front{0}.jpg"

    detect_bottom_bar(img_path)

def nothing(x):
    pass

def detect_bottom_bar(img_path_base):

    # Create bars to set threshold colors
    cv2.namedWindow('image')
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)
    cv2.createTrackbar('Lower Pixel Thresh', 'image', 0, 255, nothing)
    cv2.setTrackbarPos('Lower Pixel Thresh', 'image', 210)

    cv2.createTrackbar('Upper Pixel Thresh', 'image', 0, 255, nothing)
    cv2.setTrackbarPos('Upper Pixel Thresh', 'image', 255)

    img_num_start = 126
    img_num_end = 143
    # img_num_end = 129
    img_num_current = 126
    while(True):
        img_path = img_path_base.format(img_num_current)

        img_cv2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_height, img_width, img_bpp = np.shape(img_cv2)
        img_area = img_height * img_width
        max_object_area_threshold = img_area *.8

        img_result = img_cv2.copy()
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        lower_pixel_thresh = cv2.getTrackbarPos('Lower Pixel Thresh', 'image')
        upper_pixel_thresh = cv2.getTrackbarPos('Upper Pixel Thresh', 'image')

        img_gray = cv2.cvtColor(img_result, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(img_gray, lower_pixel_thresh, upper_pixel_thresh, cv2.THRESH_BINARY_INV)
        if(DEBUG): 
            cv2.imshow('thresh', thresh)
        im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)

        if(len(contours) == 0):
            continue

        largest_area_cnt_val = None 
        largest_cnt = None 
            
        for cnt in contours:
            area_cnt_val = cv2.contourArea(cnt)
            # Ensure contour is smaller than max threshold
            if(area_cnt_val > max_object_area_threshold):
                continue

            if(largest_area_cnt_val is None):
                largest_area_cnt_val = area_cnt_val 
                largest_cnt = cnt

            if(DEBUG):
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

            # only want closed shapes
            if(cv2.arcLength(cnt, True) is None):
                continue

            cnt_area = cv2.contourArea(cnt)
            if(cnt_area > largest_area_cnt_val):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt

        M = cv2.moments(largest_cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        # draw center point
        cv2.circle(img_result, (cx, cy), 2, (255, 0, 0), -1)

        # draw enclosing box
        rect = cv2.minAreaRect(largest_cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

        cv2.imshow('image', img_result)
        time.sleep(1)

        img_num_current += 1
        if(img_num_current > img_num_end):
            img_num_current = img_num_start

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
