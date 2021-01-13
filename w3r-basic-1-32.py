# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-31.php

# Ideas:
"""
1.  
"""

# Steps:
"""  
"""

# Notes:
"""
1. Ref: https://www.programiz.com/python-programming/examples/lcm
"""

# Code:
# Python program to find the L.C.M. of two input number
# This function computes GCD 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))



# Testing:
""" 
"""

