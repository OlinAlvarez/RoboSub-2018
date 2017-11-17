#!/usr/bin/env python2

"""
Abstract class that gives all tasks a specific structure

Initialize
Execute
Handle Results
"""

from enum import IntEnum
from collections import namedtuple

DEBUG = True
class EnumTaskStatus(IntEnum):
    NOT_STARTED = 0
    INITIALIZING = 1
    WORKING = 2
    PAUSED = 3
    FINISHED = 4


class ColorChoices(IntEnum):
    RED = 1
    GREEN = 2
    YELLOW = 3
    PINK = 4
    BOUY = 5
    FIRST_GATE = 6
    SECOND_GATE = 7

class InitializationException(Exception):
    pass

class ExecutionException(Exception):
    pass

class HandleResultsExceptions(Exception):
    pass 

Threshold = namedtuple("Threshold", ['saturation', 'hue'])

class BaseTask(object):
    hsv_colors_list = { ColorChoices.RED :[211,85,43],
        ColorChoices.GREEN :[25,123,76],
        ColorChoices.YELLOW :[199,204,120],
        ColorChoices.PINK :[255,102,102],
        ColorChoices.BUOY :[101,240,127],
        ColorChoices.FIRST_GATE :[122,168,122], 
        ColorChoices.SECOND_GATE :[0,0,0] }

    color_threshold_list = [Threshold(10,60),
        Threshold(20,70),
        Threshold(50,150),
        Threshold(0,0),
        Threshold(0,0),
        Threshold(6,52),
        Threshold(0,0)]

    def __init__(self):
        self._task_name = ""
        self._task_status = EnumTaskStatus.NOT_STARTED

    def get_task_status(self):
        return self._task_status

    def get_task_name(self):
        return self._task_name

    def run_task(self):
        self.initialize()

        self.execute()

        self.handle_results()

    def initialize(self):
        self._task_status = EnumTaskStatus.INITIALIZING
        return

    def execute(self):
        self._task_status = EnumTaskStatus.WORKING
        return

    def handle_results(self):
        self._task_status = EnumTaskStatus.FINISHED
        return

    def print_debug(self, msg):
        if(DEBUG):
            print msg
