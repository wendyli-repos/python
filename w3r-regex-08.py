# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-8.php
# Ideas:
"""
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
def uppercaseletter_lowercaseletter(string):
  patterns = "[A-Z]+[a-z]+$"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(uppercaseletter_lowercaseletter("AaBbGg"))
print(uppercaseletter_lowercaseletter("Python"))
print(uppercaseletter_lowercaseletter("python"))
print(uppercaseletter_lowercaseletter("PYTHON"))
print(uppercaseletter_lowercaseletter("aA"))
print(uppercaseletter_lowercaseletter("Aa"))