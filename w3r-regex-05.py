# 5. Write a Python program that matches a string that has an a followed by three 'b'.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-5.php
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
def is_has_three_bs(string):
  # Solution 1:
  '''
  patterns = "ab+"
  x = re.search(patterns, string)
  if x and len(x.group()) == 4:
    return f'Found a match!, {x.group()}'
  '''

  # Solution 2:
  patterns = "ab{3}"
  if re.search(patterns, string):
    return f'Found a match!', string
  else:
    return f'Not matched!'

# Testing:
print(is_has_three_bs("a")) 
print(is_has_three_bs("abc")) 
print(is_has_three_bs("abbc")) 
print(is_has_three_bs("abbbc")) 
print(is_has_three_bs("babc")) 
print(is_has_three_bs("ac")) 
print(is_has_three_bs("bcabb")) 
print(is_has_three_bs("abbb"))
print(is_has_three_bs("aabbbbbc"))
