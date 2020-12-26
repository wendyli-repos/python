# 10. Write a Python program that matches a word at the beginning of a string.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-10.php
# Ideas:
"""
1. \w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.
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
def begin_with_a_word(string):
  patterns = "^\w+"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(begin_with_a_word("The quick brown fox jumps over the lazy dog."))
print(begin_with_a_word(" The quick brown fox jumps over the lazy dog."))
