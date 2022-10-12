#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################


try:
    import threading
except (ImportError, ModuleNotFoundError) as exception:
    raise exception

try:
    import functools
except (ImportError, ModuleNotFoundError) as exception:
    raise exception


# Threaded function snippet returning a callback when the function has finished
def single_threaded(callback_function=None, daemon=False):
    def decorator(function):
        """
            This Decorator receives a function as a callable object.
            Then it wraps said function and executes it asynchronously.

            param function: Function to be executed.
            param callback_function: Callback Function
            param daemon: Boolean
            :return: thread
        """

        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            def do_callback():
                callback_function(function(args, kwargs))

            if callback_function is not None:
                thread = threading.Thread(target=do_callback, daemon=daemon)
            else:
                thread = threading.Thread(target=function, args=(args,), daemon=daemon)
            thread.start()
            return thread

        return wrapper
    return decorator
