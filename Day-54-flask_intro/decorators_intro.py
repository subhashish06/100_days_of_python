"""
Program: Timing Functions with a decorator
Author: Subhashish Dhar
Date: 04/10/2021
"""

import time


def speed_calc_decorator(function):
    """decorator function to calculate code execution time"""

    def wrapper_function():
        print(f"Executing {function.__name__}")
        start_time = time.time()
        function()
        end_time = time.time()
        code_running_time = end_time - start_time
        print(f"This code took {code_running_time} to run.")

    return wrapper_function


@speed_calc_decorator
def fast_function():
    """fast function"""
    result = 0
    for i in range(10000000):
        result = i * i
    return result


@speed_calc_decorator
def slow_function():
    """slow function"""
    result = 0
    for i in range(100000000):
        result = i * i
    return result


fast_function()
slow_function()
