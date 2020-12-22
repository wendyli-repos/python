# 2. Write a Python program to converting an Integer to a string in any base.
# Question: 
# Input: 2835,16
# Output: B13
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-2.php
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
def to_string(n,base):
   conver_tString = "0123456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]


# Testing:
print(to_string(2835,16))

