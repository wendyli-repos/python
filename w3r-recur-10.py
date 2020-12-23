# 10. Write a Python program to calculate the value of 'a' to the power 'b'.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-10.php
# Ideas:
"""
1. Be careful of the edge case which when b = 0 or a = 0 or b = 1
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
def power(a, b):
  if a == 0:
    result = 0
  elif b == 0 and a != 0:
    result = 1
  elif b == 1:
    result = a
  else:
    result = a * power(a, b-1)
  return result

# Testing:
print(power(3, 4))
print(power(0, 4))
print(power(4, 0))
print(power(0, 0))

