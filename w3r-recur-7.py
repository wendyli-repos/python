# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# Question: 
# Input: sum_series(6) -> 12
#        sum_series(10) -> 30
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-7.php
# Ideas:
"""
1. The recursion is to let each result to minus 2
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
def sum_series(n):
  if n < 1:
    return 0
  else:
    result = n - 2
    result = n + sum_series(result)
    return result

# Testing:
print(sum_series(10))

