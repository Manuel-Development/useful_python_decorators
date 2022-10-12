#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################


try:
    import multiprocessing
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

try:
    import functools
except (ImportError, ModuleNotFoundError) as exception:
    raise exception


# Threaded function snippet returning a callback when the function has finished
def single_processed(callback_function=None, daemon=False):
    def decorator(function):
        """
            This Decorator receives a function as a callable object.
            Then it wraps said function and executes it asynchronously.

            param function: Function to be executed.
            param callback_function: Callback Function
            param daemon: Boolean
            :return: thread
        """
        multiprocessing.freeze_support()

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            def do_callback():
                callback_function(function(args, kwargs))

            if callback_function is not None:
                process = multiprocessing.Process(target=do_callback, daemon=daemon)
            else:
                process = multiprocessing.Process(target=function, args=(args,), daemon=daemon)
            process.start()
            return process

        return wrapper

    return decorator
