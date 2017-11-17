#!/usr/bin/env python2

"""
Purpose of the class is to create the proper task given the task number
"""
from enum import IntEnum

from take_picture import TakeOpenCVPicture
from find_gate_task import FindGateTask

class TaskEnum(IntEnum):
    # My test task
    ALVIN_TAKE_IMG = 0

    BUOY_INIT = 1
    BUOY_RUN = 2
    GATE_INIT = 3
    GATE_RUN = 4

class TaskFactory:
    @staticmethod
    def create_task(enum_task, topic_msg, camera_manager_obj):
        if(enum_task == TaskEnum.ALVIN_TAKE_IMG):
            return TakeOpenCVPicture(topic_msg, camera_manager_obj)
        elif(enum_task == TaskEnum.GATE_RUN):
            return FindGateTask(topic_msg, camera_manager_obj)
        else:
            raise NotImplementedError("{0} is not currently implemented".format(str(enum_task)))

