# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-14.php
# Ideas:
"""
1. Question's requirement is to return a string that contains only characters (only return if matches all four). 
"""

# Steps:
"""  
1. 
"""

# Notes:
"""
1. (Maybe) best practice to using regex is to define patterns first
   Then apply .search(patterns. text) to get result
"""

# Code:
from timer import Timer

import re

@Timer.timer
def only_chars(string):
  patterns = "^[a-zA-Z0-9_]*$"  # start with a word, may appear zero or more occurances, then end with a word
  x = re.search(patterns, string)
  if x:
    return f'Found a match! {x.group()}'
  else:
    return f'No match!'

# Testing:
print(only_chars("The quick brown fox jumps over the lazy dog."))
print(only_chars("Pyth'onEx\erc#$%^&*()!_~+ises"))
print(only_chars("PythonExerci__se s"))
print(only_chars("PythonExerci__se_1"))
