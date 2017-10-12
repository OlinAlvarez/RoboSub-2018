#!/usr/bin/env python2

"""
Purpose of the class is to create the proper objective given the objective number
"""
from enum import IntEnum

from take_picture_save_objective import TakeOpenCVPictureAndSave
class ObjectiveEnum(IntEnum):
    # My test task
    ALVIN_TAKE_IMG = 0

    BUOY_INIT = 1
    BUOY_RUN = 2
    GATE_INIT = 3
    GATE_RUN = 4

class ObjectiveFactory:
    @staticmethod
    def create_objective(enum_objective, *args, **kargs):
        """
        Allows passing of arguments to constructor of BaseObjective subclasses
        """
        if(enum_objective == ObjectiveEnum.ALVIN_TAKE_IMG):
            return TakeOpenCVPictureAndSave(*args, **kargs)
        else:
            raise NotImplementedError("{0} is not currently implemented".format(str(enum_task)))

