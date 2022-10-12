#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################

try:
    import concurrent.futures
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

try:
    import functools
except (ImportError, ModuleNotFoundError) as exception:
    raise exception


def multi_threaded(function, workers=None) -> iter:
    """
    This Decorator receives a function as a callable object.
    Then it wraps said function and executes it in parallel.

    param function: Function to be executed.
    param chunks: Number of parallel Threads
    :return: Iterator from ThreadPoolExecutor
    """

    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            results = executor.map(function, *args, **kwargs)
        return results

    return wrapped
