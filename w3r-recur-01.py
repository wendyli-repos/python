# 1. Write a Python program to calculate the sum of a list of numbers.
# Question: 
# Input: [2, 4, 5, 6, 7]
# Output: 24
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-1.php
# Ideas:
"""
1. 
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
def list_sum(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    return lst[0] + list_sum(lst[1:])

@Timer.timer
def getSum(lst):
  sum = 0
  for i in range(len(lst)):
    sum += lst[i]
  return sum

# Testing:
print(list_sum([2, 4, 5, 6, 7,2, 4, 5, 6, 7,2, 4, 5, 6, 7,2, 4, 5, 6, 7]))
print(getSum([2, 4, 5, 6, 7,2, 4, 5, 6, 7,2, 4, 5, 6, 7,2, 4, 5, 6, 7]))


