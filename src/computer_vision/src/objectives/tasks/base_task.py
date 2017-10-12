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
    PROCESSING_RESULTS = 4
    FINISHED = 5

class InitializationException(Exception):
    pass

class ExecutionException(Exception):
    pass

class HandleResultsException(Exception):
    pass 

class TaskFailedException(Exception):
    pass

class BaseTask(object):
    def __init__(self, task_name):
        self._task_name = task_name
        self._task_status = EnumTaskStatus.NOT_STARTED
        self._input_data = None
        self._output_data = None

    def get_status(self):
        return self._task_status

    def get_name(self):
        return self._task_name

    def run_task(self, input_data = None):
        self._input_data = input_data

        self.initialize()

        self.execute()

        self.handle_results()

        return self._output_data

    def initialize(self):
        self._task_status = EnumTaskStatus.INITIALIZING
        return

    def execute(self):
        self._task_status = EnumTaskStatus.WORKING
        return

    def handle_results(self):
        self._task_status = EnumTaskStatus.PROCESSING_RESULTS
        return
