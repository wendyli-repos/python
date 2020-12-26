# 3. Write a Python program that matches a string that has an a followed by one or more b's.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-3.php
# Ideas:
"""
1. Regex pattern + to march One or more occurrences
2. .findall() to return all matched result
3. Pattern is to find a that either has:
  - 'a' + (one) 'b'
  - 'a' + (more) 'b'
  Note the return result is 'a', not the combination with 'b's
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
def is_has_at_least_one_ab(string):
  patterns = "ab+?"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'
  


# Testing:
print(is_has_at_least_one_ab("ac")) 
print(is_has_at_least_one_ab("abc")) 
print(is_has_at_least_one_ab("abbc")) 
print(is_has_at_least_one_ab("aabbc")) 
print(is_has_at_least_one_ab("babc")) 
print(is_has_at_least_one_ab("bc")) 
print(is_has_at_least_one_ab("bca")) 
