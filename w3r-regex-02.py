# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-2.php
# Ideas:
"""
1. Regex pattern * to march Zero or more occurrences
2. .findall() to return all matched result
3. Pattern is to find a that either has:
  - 'a' + (zero) 'b'
  - 'a' + (more) 'b'
  Note the return result is 'a', not the combination with 'b's
4. ?  # 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
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
def is_has_any_ab(string):
  # Solution 1:
  x = re.findall("ab*?", string)
  print(x)
  return bool(x)

  # Solution 2: 
  '''
  patterns = 'ab*?'
  result = re.search(patterns, string)
  print(result)
  return bool(result)
  '''


# Testing:
print(is_has_any_ab("ac")) 
print(is_has_any_ab("abc")) 
print(is_has_any_ab("abbc")) 
print(is_has_any_ab("aabbc")) 
print(is_has_any_ab("babc")) 
print(is_has_any_ab("bc")) 
print(is_has_any_ab("bca")) 
