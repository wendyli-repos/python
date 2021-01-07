# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Question: 
# Input: Sample value of n is 5
# Output: Expected Result : 615
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-10.php

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
base = input("Pls enter an integer: ")
value = ""
values = []
  
for _ in range(1, 4):
  value += base
  values.append(int(value))
  
print(sum(values))

# Testing:
""" 
"""

