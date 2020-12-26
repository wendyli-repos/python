# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-9.php
# Ideas:
"""
1. The question mark symbol ? matches zero or one occurrence of the pattern left to it.
2. The star symbol * matches zero or more occurrences of the pattern left to it.
3. 
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
  patterns = "a.*?b$"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(uppercaseletter_lowercaseletter("aabbbb"))
print(uppercaseletter_lowercaseletter("aabAbbbc"))
print(uppercaseletter_lowercaseletter("accddbbjjjb"))
