# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-23.php

# Ideas:
"""
1.  
"""

# Steps:
"""  
"""

# Notes:
"""
"""

# Code:
def copySubstring(str, n):
  # version 1: with two for loops
  # result = ""
  # if len(str) >= 2:
  #   for _ in range(n):
  #     result += str[:2]
  #   return result
  # else:
  #   for _ in range(n):
  #     result += str
  #   return result

  # version 2: refactor using one for loop
  if len(str) >= 2:
    substr = str[:2]
  else:
    substr = str
    
  result = ""
  for _ in range(n):
    result += substr
  return result

print(copySubstring("h", 3))
print(copySubstring("hello", 5))


# Testing:
""" 
"""

