# 15. Write a Python program where a string will start with a specific number.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-15.php
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
def start_with_5(string):
  patterns = "^5"  
  x = re.search(patterns, string)
  if x:
    return f'Found a match! {x.group()}'
  else:
    return f'No match!'

# Testing:
print(start_with_5("5-2345861"))
print(start_with_5("6-2345861"))

