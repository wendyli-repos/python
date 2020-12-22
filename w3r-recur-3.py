# 3. Write a Python program of recursion list sum.
# Question: 
# Input: [1, 2, [3,4], [5,6]]
# Output: 21
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-3.php
# Ideas:
"""
1. typeof
"""

# Steps:
"""  
1. Check type of each list element
2. if element is a list, then recurse
"""

# Notes:
"""
1. 
"""

# Code:
from timer import Timer

@Timer.timer
def recursionListSum(lst):
  total = 0
  for element in lst:
    if (type(element)) == type([]):
      total += recursionListSum(element)
    else:
      total += element
  return total

# Testing:
print(recursionListSum([1, 2, [3,4], [5,6]]))
print(type([]))
