# 17. Write a Python program to check for a number at the end of a string.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-17.php
# Ideas:
"""
1.  
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
def ends_with_numbers(string):
  patterns = ".*[0-9]$"  
  x = re.search(patterns, string)
  if x:
    return f'Found a match! {x.group()}'
  else:
    return f'No match!'

# Testing:
print(ends_with_numbers("abcdef"))
print(ends_with_numbers("abcdef6"))
