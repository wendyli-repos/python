# 4. Write a Python program to get the factorial of a non-negative integer.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-4.php
# Ideas:
"""
1. Note 0! = 1, 1! = 1
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
def getFactorial(n):
  if n <= 1:
    factorial = 1
  else:
    factorial = n * getFactorial(n - 1)
  return factorial

# Testing:
print(getFactorial(5))

