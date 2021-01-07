# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Question: 
# Input: Sample filename : abc.java
# Output: java
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-7.php

# Ideas:
"""
1.
"""

# Steps:
"""  
"""

# Notes:
"""
1. str() 
2. repr() returns a string with quotes & value is more accurate than str()
"""

# Code:
fileName = input("Pls enter full file name with extension: ")
extension = repr(fileName.split(".")[-1])  # return the last element from a list incase file name contians a "."
print(extension)
        

# Testing:
""" 
"""

