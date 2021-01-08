# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-19.php

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
import re
def checkIS(str):
  # S1: string slice
  # if len(str) >= 2 and str[0:1] == "Is":
  #   return str
  # else: 
  #   return "Is" + str

  # S2: regex, starts with "Is"
  hasIs = re.findall("^Is", str)
  if len(str) >= 2 and hasIs:
    return str
  else:
    return "Is" + str

print(checkIS("Array"))
print(checkIS("IsEmpty"))

# Testing:
""" 
"""

