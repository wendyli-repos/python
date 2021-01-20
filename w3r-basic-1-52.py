# 52. Write a Python program to print to stderr.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-52.php

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
import sys
from __future__ import print_function

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")

# Testing:
""" 
"""

