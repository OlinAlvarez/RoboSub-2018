#!/usr/bin/env python2
"""
Objectives will contain all the tasks required to accomplish objective.

Tasks can generally take input and return an output. Therefore, we can chain tasks together.
"""

from enum import IntEnum

class ObjectiveStatusEnum(IntEnum):
    NOT_STARTED = 0
    SUCCESS = 1
    FAILED = 2

class BaseObjective(object):
    def __init__(self, objective_name, task_list = None, max_objective_retries = 1):
        self._objective_name = objective_name

        if(task_list is None):
            self._task_list = list()
        else:
            self._task_list = task_list

        self._working_task_index = 0
        self._final_result_data = None
        self._max_retries = max_objective_retries
        self._objective_status = ObjectiveStatusEnum.NOT_STARTED

    def get_name(self):
        return self._objective_name

    def get_task_list(self):
        return self._task_list

    def get_status(self):
        return self._objective_status

    def start_objective(self, initial_input = None):
        task_list_count = len(self._task_list)

        for attempt in range(self._max_retries):
            task_index = 0
            try:
                # First task, pass in initial data if needed
                # Last task, store data into final result container
                for task_index in range(task_list_count):
                    if 0 == task_index:
                        result_data = self._task_list[task_index].run_task(initial_input)
                    elif (task_list_count - 1) == task_index:
                        self._final_result_data = self._task_list[task_index].run_task(result_data)
                    else:
                        result_data = self._task_list[task_index].run_task(result_data)

                self._objective_status = ObjectiveStatusEnum.SUCCESS
                return
            except Exception as e:
                print "Exception: '{0}'".format(str(e))
                print "Objective '{0}' failed on task '{1}'.".format(self._objective_name, self._task_list[task_index].get_name())
                
                if(attempt < self._max_retries):
                    print "Attempting {0}/{1} objective retries".format(attempt, self._max_retries)

        self._objective_status = ObjectiveStatusEnum.FAILED
