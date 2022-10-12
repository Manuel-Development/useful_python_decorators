#!/usr/bin/env python
# -*- coding: utf-8 -*-

########################################################################################################################
"""

"""

__author__ = ""
__copyright__ = ""

########################################################################################################################

from .decorator_multithreading import multi_threaded
from .decorator_multiprocessing import multi_processed

from .decorator_singlethreading import single_threaded
from .decorator_singleprocessing import single_processed

__all__ = ["multi_threaded", "multi_processed",
           "single_threaded", "single_processed"]
