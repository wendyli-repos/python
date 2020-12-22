# 6. Write a Python program to get the sum of a non-negative integer.
# Question: 
# Input: sumDigits(345) -> 12
#        sumDigits(45) -> 9
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-6.php
# Ideas:
"""
1. integer division
"""

# Steps:
"""  
"""

# Notes:
"""
1. 
"""

# Code:
from timer import Timer

@Timer.timer
def sumDigits(n):
  if n == 0:
    result = 0
  else:
    result = n % 10 + sumDigits(int(n / 10))
  return result

# Testing:
print(sumDigits(345))

