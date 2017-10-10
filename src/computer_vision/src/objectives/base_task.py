#!/usr/bin/env python2

"""
Abstract class that gives all tasks a specific structure

Initialize
Execute
Handle Results
"""

from enum import IntEnum

class EnumTaskStatus(IntEnum):
    NOT_STARTED = 0
    INITIALIZING = 1
    WORKING = 2
    PAUSED = 3
    FINISHED = 4

class InitializationException(Exception):
    pass

class ExecutionException(Exception):
    pass

class HandleResultsExceptions(Exception):
    pass 

class BaseTask(object):
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
