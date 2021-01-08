# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
# Question: Testing is a number is between 900-1100 or 1900-2100.
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-17.php

# Ideas:
"""
1.  
"""

# Steps:
"""  
"""

# Notes:
"""
1. Stackoverflow question: https://stackoverflow.com/questions/48906960/python-test-whether-a-number-is-within-100-of-1000-or-2000/48907378
"""

# Code:
def distance(n):
  return abs(n - 1000) <= 100 or abs(n - 2000) <= 100

print(distance(50))
print(distance(1800))

# Testing:
""" 
"""

