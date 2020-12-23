# 8. Write a Python program to calculate the harmonic sum of n-1.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-8.php
# Ideas:
"""
1. 
"""

# Steps:
"""  
"""

# Notes:
"""
1. The harmonic sum is the sum of reciprocals of the positive integers.
"""

# Code:
from timer import Timer

@Timer.timer
def harmonic_sum(n):
  if n == 1:
    result = 1 / n
  else: 
    result = 1 / n + harmonic_sum(n - 1)
  return result

# Testing:
print(harmonic_sum(7))

