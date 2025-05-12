"""
    Create a function decorator that prints a timestamp (in a form like year-month-day hour:minute:seconds, eg. 2019-11-05 08:33:22)
    Create a few ordinary functions that do some simple tasks, like adding or multiplying two numbers.
    Apply your decorator to those functions to ensure that the time of the function executions can be monitored.
"""

import datetime


def time_monitor(own_function):
    def wrapper(*args):
        now = datetime.datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        print(timestamp_str)
        return own_function(*args)
    return wrapper

@time_monitor
def add(*args):
    j = lambda *args: sum(args)
    return j(*args)

@time_monitor    
def mul(x , y):
    return x * y
    


print(add(3,4))
print(mul(3,4))