# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Question: 
# Input: 3, 5, 7, 23
# Output: List : ['3', ' 5', ' 7', ' 23']
#         Tuple : ('3', ' 5', ' 7', ' 23')
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-6.php

# Ideas:
"""
1.
"""

# Steps:
"""  
"""

# Notes:
"""
1. Used strip() to delete all spaces
"""

# Code:
numbers = input("Pls enter a sequence of comma-separated numbers: ")
generatedList = []
for i in numbers.split(","):
  generatedList.append(i.lstrip()) 
generatedTuple = tuple(generatedList)
print("List: ", generatedList)
print("Tuple: ", generatedTuple)
        

# Testing:
""" 
"""

