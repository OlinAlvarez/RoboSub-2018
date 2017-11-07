#!/usr/bin/env python2

import cv2
import numpy as np
import time
from utils.color_manager import OpenCVColor

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
    target_color_obj = OpenCVColor(r_hardcode, g_hardcode, b_hardcode)

    while(True):
        leading_bar_found = False
        img_path = img_path_base.format(img_num_current)

        # Increment number
        img_num_current += 1
        if(img_num_current > img_num_end):
            img_num_current = img_num_start


        img_cv2 = cv2.imread(img_path, cv2.IMREAD_COLOR)
        img_height, img_width, img_bpp = np.shape(img_cv2)
        img_area = img_height * img_width
        max_object_area_threshold = img_area *.8
        min_object_area_threshold = img_area * .0002

        img_result = img_cv2.copy()

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        hsv_hue_thresh = cv2.getTrackbarPos('HSV Thresh', 'image')
        lower_pixel_thresh = cv2.getTrackbarPos('Lower Pixel Thresh', 'image')
        upper_pixel_thresh = cv2.getTrackbarPos('Upper Pixel Thresh', 'image')
        sigmaColor = cv2.getTrackbarPos('SigmaColor', 'image')
        sigmaSpace = cv2.getTrackbarPos('SigmaSpace', 'image')

        # Smoothen out image but keep sharp edges
        img_blurred = cv2.bilateralFilter(img_result, 9, sigmaColor, sigmaSpace)

        if(DEBUG):
            cv2.imshow("blurred_img", img_blurred)
            cv2.moveWindow("blurred_img", 0,700)

        # Convert bgr image to hsv 
        img_hsv = cv2.cvtColor(img_blurred, cv2.COLOR_BGR2HSV)

        # Obtain color we want to filter on
        target_color_obj.set_rgb([r, g, b])
        lower_bar_hsv = np.array(target_color_obj.get_hsv_lower_bound(hsv_hue_thresh))
        upper_bar_hsv = np.array(target_color_obj.get_hsv_upper_bound(hsv_hue_thresh))

        # Create mask and filter out what we want
        img_mask = cv2.inRange(img_hsv, lower_bar_hsv, upper_bar_hsv)
        img_color_filtered = cv2.bitwise_and(img_blurred, img_blurred, mask = img_mask)

        if(DEBUG):
            cv2.imshow("img_color_filtered", img_color_filtered)
            cv2.moveWindow("img_color_filtered", 800, 800)

        img_gray = cv2.cvtColor(img_color_filtered, cv2.COLOR_BGR2GRAY)
        im2, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        cv2.imshow("Original Image", img_cv2)
        cv2.moveWindow("Original Image", 900, 0)
        if(not DEBUG):
            time.sleep(1)

        if(len(contours) == 0):
            print "Leading bar not found."
            img_result = cv2.putText(img_result, "Leading bar not found.", (100,100), cv2.FONT_HERSHEY_PLAIN, 2, 255, thickness = 4)
            cv2.imshow('image', img_result)
            continue

        largest_area_cnt_val = None 
        largest_cnt = None 
        
        for cnt in contours:
            area_cnt_val = cv2.contourArea(cnt)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)

            # We only want rectangles
            vertices_count = len(approx)
            if(not(vertices_count >= lower_vertices_count and vertices_count <= upper_vertices_count)):
                if(DEBUG):
                    print "Upper vertices bound: {0} - Lower vertcies bound: {1} - Found vertices count: {2}".format(upper_vertices_count, lower_vertices_count, str(vertices_count))
                continue

            # Ensure contour area is within specified threshold
            if(area_cnt_val > max_object_area_threshold or area_cnt_val < min_object_area_threshold):
                if(DEBUG):
                    print "area_cnt_val {0} - max_area {1} - min_area{2}".format(area_cnt_val, max_object_area_threshold, min_object_area_threshold)
                continue

            # We are not looking for more rectangular shapes. Circular shapes tend to have many more points
            if(len(cnt) > 50):
                continue

            if(DEBUG):
                rect = cv2.minAreaRect(cnt)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

                # Write the amount of contours found on the detected object
                M = cv2.moments(cnt)
                if(M['m00'] != 0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M['m01']/M['m00'])
                    img_result = cv2.putText(img_result, str(len(cnt)), (cx,cy), cv2.FONT_HERSHEY_PLAIN, 2, 255)

            cnt_area = cv2.contourArea(cnt)

            # If there is only one and it passes all our checks, it is MOST LIKELY the leading bar..
            leading_bar_found = True
            if(largest_area_cnt_val is None):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt
            elif(cnt_area > largest_area_cnt_val):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt

        if(DEBUG):
            print "Largest contour area: " + str(largest_area_cnt_val)
            print "Image area: " + str(img_area)

        # Only plot if we found something
        if(not leading_bar_found):
            print "Leading bar not found."
            img_result = cv2.putText(img_result, "Leading bar not found.", (100,100), cv2.FONT_HERSHEY_PLAIN, 2, 255, thickness = 4)
            cv2.imshow('image', img_result)
            continue

        M = cv2.moments(largest_cnt)
        obj_direction = "I am lost..."
        cam_x_center = img_width / 2
        cam_x_offset = img_width * .05
        if(M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # draw center point
            cv2.circle(img_result, (cx, cy), 2, (255, 0, 0), -1)

            # Determine obj relative to camera center with threshold
            if(cx <= (cam_x_center - cam_x_offset)):
                obj_direction = "Move Sub Left"
            elif(cx >= (cam_x_center + cam_x_offset)):
                obj_direction = "Move Sub Right"
            else:
                obj_direction = "Relatively Centered"

        # draw enclosing box
        rect = cv2.minAreaRect(largest_cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

        # Where is object relative to center
        img_result = cv2.putText(img_result, obj_direction, (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, 255, thickness = 4)
        img_result = cv2.line(img_result, (cam_x_center, 0), (cam_x_center, img_height), (0, 255, 0), 2)
        cv2.imshow('image', img_result)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
