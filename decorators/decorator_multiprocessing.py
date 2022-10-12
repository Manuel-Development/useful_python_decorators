#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################
import multiprocessing

try:
    import concurrent.futures
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

try:
    import functools
except (ImportError, ModuleNotFoundError) as exception:
    raise exception


def multi_processed(function, workers=None) -> iter:
    """
    This Decorator receives a function as a callable object.
    Then it wraps said function and executes it in parallel.

    param function: Function to be executed.
    param chunks: Number of parallel Processes
    :return: Iterator from ProcessPoolExecutor
    """

    multiprocessing.freeze_support()

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
            results = executor.map(function, *args, **kwargs)
        return results

    return wrapped
