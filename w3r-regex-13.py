# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-13.php
# Ideas:
"""
1. \B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.
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
def z_in_middle(string):
  patterns = "\Bz\B"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(z_in_middle("The quick brown fox jumps over the lazy dog."))
print(z_in_middle("Python Exercises."))
