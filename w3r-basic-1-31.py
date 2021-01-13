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
1. Ref: https://baike.baidu.com/item/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%AE%97%E6%B3%95#:~:text=%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%AE%97%E6%B3%95%E5%8F%88%E7%A7%B0%E8%BE%97%E8%BD%AC%E7%9B%B8%E9%99%A4%E6%B3%95,b%2Ca%20mod%20b)%E3%80%82
"""

# Code:
# Python program to demonstrate Basic Euclidean Algorithm   
# Function to return gcd of a and b 
def gcd(a, b):  
    if a == 0 : 
        return b  
    return gcd(b%a, a) 
  
a = 10
b = 15
print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# a = 35
# b = 10
# print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# a = 31
# b = 2
# print("gcd(", a , "," , b, ") = ", gcd(a, b)) 
  
# Code Contributed By Mohit Gupta_OMG <(0_o)> 


# Testing:
""" 
"""

