#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################

# Imports for the Application
try:
    import time
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

try:
    import multiprocessing
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

from decorators import multi_threaded, multi_processed

from decorators import single_threaded, single_processed


@single_threaded()
def single_thread_function(data):
    print(data)
    time.sleep(2)
    return data


@single_processed()
def single_process_function(data):
    print(data)
    time.sleep(1)
    return data


def multi_function(data):
    print(data)
    time.sleep(1)
    return data


if __name__ == '__main__':
    data_list = []
    [data_list.append("I am here {} ".format(i)) for i in range(0, 100)]

    #[single_thread_function(data) for data in data_list]

    #[single_process_function(data) for data in data_list]

    results_threaded = multi_threaded(function=multi_function, workers=8)(data_list)
    """[print(results) for results in results_threaded]"""

    results_processed = multi_processed(function=multi_function, workers=8)(data_list)
    """[print(results) for results in results_processed])"""
