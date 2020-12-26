# 12. Write a Python program that matches a word containing 'z'.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-12.php
# Ideas:
"""
1. \w
2. *
3. z.
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
def word_contains_z(string):
  patterns = "\w*z.\w*"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(word_contains_z("The quick brown fox jumps over the lazy dog."))
print(word_contains_z("Python Exercises."))
