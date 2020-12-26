# 7. Write a Python program to find sequences of lowercase letters joined with a underscore.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-7.php
# Ideas:
"""
1. The caret symbol ^ is used to check if a string starts with a certain character.
2. The dollar symbol $ is used to check if a string ends with a certain character.
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
def lowercaseLetter_joined_by_underscore(string):
  patterns = "^[a-z]+_[a-z]+$"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(lowercaseLetter_joined_by_underscore("aab_cbbbc"))
print(lowercaseLetter_joined_by_underscore("aab_Abbbc"))
print(lowercaseLetter_joined_by_underscore("Aaab_abbbc"))
