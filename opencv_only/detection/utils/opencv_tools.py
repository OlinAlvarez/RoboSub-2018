#!/usr/bin/env python2
import cv2


"""
Class provides the essential functions useful for opencv
"""
def getObjectsCenter(opencv_contour):
    """
    Returns
        Tuple 
        (x, y) if found else (None, None)
    """
    M = cv2.moments(opencv_contour)
    result_tuple = (None, None)
    if(M['m00'] != 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        result_tuple = (cx, cy)

    return result_tuple

def getObjectsCenterOffset(objects_center_tuple, relative_center_origin):
    """
    Calculates the offset of the objects center relative to some origin point

    Parameters
        objects_center_tuple    (x, y)
        origin_center_tuple     (x, y)

    Returns
        Tuple (x, y)
    """
    if(not isinstance(relative_center_origin, tuple)):
        raise ValueError("origin_center_tuple is not a tuple")

    if(not isinstance(objects_center_tuple, tuple)):
        raise ValueError("objects_center_tuple is not a tuple")

    if(relative_center_origin[0] > objects_center_tuple[0]):
        offset_x = relative_center_origin[0] - objects_center_tuple[0]
    else:
        offset_x = objects_center_tuple[0] - relative_center_origin[0]

    if(relative_center_origin[1] > objects_center_tuple[1]):
        offset_y = relative_center_origin[1] - objects_center_tuple[1]
    else:
        offset_y = objects_center_tuple[1] - relative_center_origin[1]

    return (offset_x, offset_y)
