#!/usr/bin/env python2

import cv2
import numpy as np
import time
from detection.utils.color_manager import OpenCVColor
from detection.bar_detection import BarDetection, BarDetectionOptions
from detection.utils.image_metadata import ImageMetaData
import detection.utils.opencv_tools as OpenCVTools
# The purpose of this task is to ensure the camera is parallel with a bar.
# This will guide us into the direction of the bouy.

DEBUG = True
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
    cv2.createTrackbar('HSV Thresh', 'image', 0, 50, nothing)
    cv2.createTrackbar('Lower Pixel Thresh', 'image', 0, 255, nothing)
    cv2.createTrackbar('Upper Pixel Thresh', 'image', 0, 255, nothing)
    cv2.createTrackbar('SigmaColor', 'image', 0, 255, nothing)
    cv2.createTrackbar('SigmaSpace', 'image', 0, 255, nothing)


    # cv2.setTrackbarPos('Lower Pixel Thresh', 'image', 210)
    # cv2.setTrackbarPos('Upper Pixel Thresh', 'image', 255)

    # This setup provided teh cleanest edges but blurrd most.
    cv2.setTrackbarPos('SigmaColor', 'image',65)
    cv2.setTrackbarPos('SigmaSpace', 'image', 75)
    cv2.setTrackbarPos('HSV Thresh', 'image', 15)

    r_hardcode = 235
    g_hardcode = 254
    b_hardcode = 180
    cv2.setTrackbarPos('R', 'image', r_hardcode)
    cv2.setTrackbarPos('G', 'image', g_hardcode)
    cv2.setTrackbarPos('B', 'image', b_hardcode)
    
    # Adaptive thersholding
    cv2.setTrackbarPos('Upper Pixel Thresh', 'image', 2)

    if(not DEBUG):
        img_num_start = 126
        img_num_end = 144
        img_num_current = 126
    else:
        img_num_start = 126
        img_num_end = 126
        img_num_current = 126

    upper_vertices_count = 8
    lower_vertices_count = 3

    # Start with object out here so we are not recreating every time..
    # target_color_obj = OpenCVColor(r_hardcode, g_hardcode, b_hardcode)

    # BarDetection
    bar_detection_options = BarDetectionOptions()
    bar_detector = BarDetection(bar_detection_options)

    # Create image meta data wrapper
    img_metadata = ImageMetaData()
    while(True):
        time.sleep(1) 
        leading_bar_found = False
        img_path = img_path_base.format(img_num_current)

        # Increment number
        img_num_current += 1
        if img_num_current > img_num_end:
            img_num_current = img_num_start

        img_cv2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_metadata.setOpenCVImg(img_cv2)

        # Using this to show image of it outlined object
        img_result = img_cv2.copy()

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # Get values from sliders
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        hsv_hue_thresh = cv2.getTrackbarPos('HSV Thresh', 'image')
        # lower_pixel_thresh = cv2.getTrackbarPos('Lower Pixel Thresh', 'image')
        # upper_pixel_thresh = cv2.getTrackbarPos('Upper Pixel Thresh', 'image')
        sigmaColor = cv2.getTrackbarPos('SigmaColor', 'image')
        sigmaSpace = cv2.getTrackbarPos('SigmaSpace', 'image')

        # Update detection options
        detection_options = bar_detector.detection_options
        detection_options.color_filter.r = r
        detection_options.color_filter.g = g
        detection_options.color_filter.b = b
        detection_options.color_filter.hue_offset = hsv_hue_thresh

        detection_options.blur.sigma_color_space = sigmaColor
        detection_options.blur.sigma_coordinate_space = sigmaSpace

        # After options updated, start detection and get results
        detection_results = bar_detector.detectBar(img_metadata)

            # if(DEBUG):
                # rect = cv2.minAreaRect(cnt)
                # box = cv2.boxPoints(rect)
                # box = np.int0(box)
                # img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

                # Write the amount of contours found on the detected object
                # M = cv2.moments(cnt)
                # if(M['m00'] != 0):
                    # cx = int(M['m10']/M['m00'])
                    # cy = int(M['m01']/M['m00'])
                    # img_result = cv2.putText(img_result, str(len(cnt)), (cx,cy), cv2.FONT_HERSHEY_PLAIN, 2, 255)

        # Only plot if we found something
        if(not detection_results.obj_detected_bool):
            print "Leading bar not found."
            img_result = cv2.putText(img_result, "Leading bar not found.", (100,100), cv2.FONT_HERSHEY_PLAIN, 2, 255, thickness = 4)
            cv2.imshow('image', img_result)
            continue


        # Draw findings!
        obj_direction = "I am lost..."
        img_x_center = img_metadata.getWidth() / 2
        img_x_offset = img_metadata.getWidth() * .05
        cx = detection_results.obj_center_tuple[0]
        cy = detection_results.obj_center_tuple[1]

        if(not(cx is None or cy is None)):
            # draw center point
            cv2.circle(img_result, (cx, cy), 2, (255, 0, 0), -1)

            # Determine obj relative to camera center with threshold
            if(cx <= (img_x_center - img_x_offset)):
                obj_direction = "Move Sub Left"
            elif(cx >= (img_x_center + img_x_offset)):
                obj_direction = "Move Sub Right"
            else:
                obj_direction = "Relatively Centered"

        # draw enclosing box
        rect = cv2.minAreaRect(detection_results.obj_contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

        # Where is object relative to center
        img_result = cv2.putText(img_result, obj_direction, (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, 255, thickness = 4)
        img_result = cv2.line(img_result, (img_x_center, 0), (img_x_center, img_metadata.getHeight()), (0, 255, 0), 2)
        cv2.imshow('image', img_result)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
