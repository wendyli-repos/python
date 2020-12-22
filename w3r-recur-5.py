# 5. Write a Python program to solve the Fibonacci sequence using recursion.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion-exercise-5.php
# Ideas:
"""
1. The Rule is Xn = X(n−1) + X(n−2)
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
def getFibonacciSeq(n):
  if n == 0:
    x = 0
  elif n == 1:
    x = 1
  else:
    x = getFibonacciSeq(n - 1) + getFibonacciSeq(n - 2)
  return x

# Testing:
print(getFibonacciSeq(3))
print(getFibonacciSeq(4))
print(getFibonacciSeq(5))
print(getFibonacciSeq(6))
print(getFibonacciSeq(7))
print(getFibonacciSeq(8))
print(getFibonacciSeq(9))

