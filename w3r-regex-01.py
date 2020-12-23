# 1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-1.php
# Ideas:
"""
1. Regex pattern [a-zA-Z0-9]
2. .compile()
3. .search()
"""

# Steps:
"""  
1. Using .compile() to create a Regex Object
2. Using .search() to check is string contains patterns
  Note: .search() returns the matching object from the string to check. 
        Return type is an object. 
        >>> <re.Match object; span=(0, 1), match='*'>
3. Return boolean result
"""

# Notes:
"""
1. 
"""

# Code:
from timer import Timer

import re

@Timer.timer
def is_allowed_specific_char(string):
  charRe = re.compile(r'[^a-zA-Z0-9]')
  string = charRe.search(string)
  print(string)
  return not bool(string)

# Testing:
print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
