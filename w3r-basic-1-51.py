# 51. Write a Python program to determine profiling of Python programs. 
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-51.php

# Ideas:
"""
1. A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
"""

# Steps:
"""  
"""

# Notes:
"""
1. Ref: https://www.oreilly.com/library/view/python-standard-library/0596000960/ch11s05.html
2. Ref: https://www.machinelearningplus.com/python/cprofile-how-to-profile-your-python-code/
"""

# Code:
# S1: 
import pstats 
import profile
def func1():
  print(1 + 2)

p = profile.Profile()
p.run("func1()")

s = pstats.Stats(p)
s.sort_stats("time", "name").print_stats()

#S2
import cProfile
def sum():
  print(1 + 2)
cProfile.run("sum()")
# Testing:
""" 
"""

