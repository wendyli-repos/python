# 57. Write a program to get execution time (in seconds) for a Python method.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-57.php

# Ideas:
"""
"""

# Steps:
"""  
"""

# Notes:
"""
"""

# Code:

import functools
import time

class Timer():
  def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
      tic = time.perf_counter()
      value = func(*args, **kwargs)
      toc = time.perf_counter()
      elapsed_time = toc - tic
      print(f"Elapsed time: {elapsed_time:0.4f} seconds")
      return value
    return wrapper_timer

@Timer.timer
def func1():
  for i in range(0, 10):
    print('*', end="")
  print("\n")

func1()
# Testing:
""" 
"""

