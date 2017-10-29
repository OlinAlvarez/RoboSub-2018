#!/usr/bin/env python2

import cv2
import numpy as np
import time

# The purpose of this task is to ensure the camera is parallel with a bar.
# This will guide us into the direction of the bouy.

#DEBUG = True
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
    cv2.setTrackbarPos('R', 'image', 235)
    cv2.setTrackbarPos('G', 'image', 254)
    cv2.setTrackbarPos('B', 'image', 180)
    
    # Adaptive thersholding
    cv2.setTrackbarPos('Upper Pixel Thresh', 'image', 2)

    if(not DEBUG):
        img_num_start = 126
        img_num_end = 143
        img_num_current = 126
    else:
        img_num_start = 141
        img_num_end = 141
        img_num_current = 141
    while(True):
        img_path = img_path_base.format(img_num_current)

        # Increment number
        img_num_current += 1
        if(img_num_current > img_num_end):
            img_num_current = img_num_start


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

        # Filter out color to eliminate noise
        img_hsv = cv2.cvtColor(img_blurred, cv2.COLOR_BGR2HSV)
        hsv_color_wanted = cv2.cvtColor(np.uint8([[[b,g,r]]]), cv2.COLOR_BGR2HSV)[0][0]
        
        wanted_hsv_hue = hsv_color_wanted[0]
        # Utilizes numpy's unit 8 datatype and overflowing to calculate hue boudnaries
        if(hsv_hue_thresh > wanted_hsv_hue or (hsv_hue_thresh + wanted_hsv_hue) > 255): 
            hsv_hue_thresh += 1
        lower_hue = np.uint8(wanted_hsv_hue - hsv_hue_thresh)
        upper_hue = np.uint8(wanted_hsv_hue + hsv_hue_thresh)
        lower_bar_hsv = np.array([lower_hue, 50, 50])
        upper_bar_hsv = np.array([upper_hue, 255, 255])

        # Create mask and filter out what we want
        img_mask = cv2.inRange(img_hsv, lower_bar_hsv, upper_bar_hsv)
        img_color_filtered = cv2.bitwise_and(img_blurred, img_blurred, mask = img_mask)

        if(DEBUG):
            cv2.imshow("img_color_filtered", img_color_filtered)
            cv2.moveWindow("img_color_filtered", 800, 800)

        img_gray = cv2.cvtColor(img_color_filtered, cv2.COLOR_BGR2GRAY)

        # ================ Want to removethresholding=====================
        # ret, thresh = cv2.threshold(img_gray, lower_pixel_thresh, upper_pixel_thresh, cv2.THRESH_BINARY)
    
        # Adaptive Thresholding for images with different lighting
        #thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,  upper_pixel_thresh)

        #if(DEBUG): 
            #cv2.imshow('thresh_img', thresh)
            #cv2.moveWindow("thresh_img", 700, 0)
        #im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # ================ Want to removethresholding=====================

        im2, contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if(len(contours) == 0):
            continue

        largest_area_cnt_val = None 
        largest_cnt = None 
        
        for cnt in contours:
            area_cnt_val = cv2.contourArea(cnt)
            #peri = cv2.arcLength(cnt, True)
            #approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)

            # We only want rectangles
            #vertices_count = len(approx)
            #if(vertices_count != 4):
                #continue

            # Ensure contour is smaller than max threshold
            if(area_cnt_val > max_object_area_threshold):
                continue

            # We are not lookign for circular shapes. Circular shapes tend to have many more points
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

            # If there is only one and it passes all our checks, take it.
            if(largest_area_cnt_val is None):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt
            elif(cnt_area > largest_area_cnt_val):
                largest_area_cnt_val = cnt_area
                largest_cnt = cnt

        M = cv2.moments(largest_cnt)
        if(M['m00'] != 0):
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

            # draw center point
            cv2.circle(img_result, (cx, cy), 2, (255, 0, 0), -1)

        # Only plot if we found something
        if(largest_cnt is None):
            print "Leading bar not detected.."

            continue

        # draw enclosing box
        rect = cv2.minAreaRect(largest_cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        img_result = cv2.drawContours(img_result, [box], 0, (0, 0, 255), 2)

        cv2.imshow('image', img_result)
        if(not DEBUG):
            time.sleep(1)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
