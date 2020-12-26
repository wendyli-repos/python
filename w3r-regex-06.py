# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-6.php
# Ideas:
"""
1. Regex MetaCharacters {} - Braces
   Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.
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
def is_has_two_to_three_bs(string):
  patterns = "ab{2,3}"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(is_has_two_to_three_bs("a")) 
print(is_has_two_to_three_bs("abc")) 
print(is_has_two_to_three_bs("abbc")) 
print(is_has_two_to_three_bs("abbbc")) 
print(is_has_two_to_three_bs("babc")) 
print(is_has_two_to_three_bs("ac")) 
print(is_has_two_to_three_bs("bcabb")) 
print(is_has_two_to_three_bs("abbb"))
print(is_has_two_to_three_bs("aabbbbbc"))
