# 63. Write a Python program to get an absolute file path.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-63.php

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
import os
def absolute_file_path(path_fname):
  return os.path.abspath(path_fname) 

# print("Absolute file path: ",absolute_file_path("w3r-basic-1-63.py"))
print("Absolute file path: ",absolute_file_path(os.path.basename(__file__)))

# Testing:
""" 
"""

