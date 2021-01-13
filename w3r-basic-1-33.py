# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-33.php

# Ideas:
"""
1.  
"""

# Steps:
"""  
"""

# Notes:
"""
"""

# Code:
def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))


# Testing:
""" 
"""

