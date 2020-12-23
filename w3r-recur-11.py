# 11. Write a Python program to find  the greatest common divisor (gcd) of two integers. 
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-11.php
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
def Recurgcd(a, b):
  low = min(a, b)
  high = max(a, b)

  if low == 0:
    result = high
  elif low == 1:
    result = 1
  else:
    result = Recurgcd(low, high % low)
  return result

# Testing:
print(Recurgcd(12, 14))
print(Recurgcd(54, 24))
print(Recurgcd(19, 17))
