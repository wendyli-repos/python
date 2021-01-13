# 36. Write a Python program to add two objects if both objects are an integer type.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-36.php

# Ideas:
"""
1. isinsrance()
"""

# Steps:
"""  
"""

# Notes:
"""
1. https://www.geeksforgeeks.org/type-isinstance-python/
"""

# Code:
def add_numbers(x, y):
  try:
    if (isinstance(x, int) and isinstance(y, int)):
      return (x + y)
  except TypeError:
    return x + y


# print(add_numbers(3, '2'))
print(add_numbers('3', 2))
print(add_numbers(2, 2))


# Testing:
""" 
"""

