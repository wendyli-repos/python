# 9. Write a Python program to calculate the geometric sum of n-1
# Question: This quetion is to implement a series of 2. 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-9.php
# Ideas:
"""
1. 
"""

# Steps:
"""  
"""

# Notes:
"""
1. In mathematics, a geometric series is a series with a constant ratio between successive terms. 即等比数列
"""

# Code:
from timer import Timer

@Timer.timer
def geometric_sum(n):
  if n < 0:
    result = 0
  else:
    result = 1/ pow(2, n) + geometric_sum(n-1)
  return result

# Testing:
print(geometric_sum(4))

