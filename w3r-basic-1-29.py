# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. 
# Question: 
# Input: 
"""
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
"""
# Output: {'Black', 'White'}
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-29.php

# Ideas:
"""
1.  
"""

# Steps:
"""  
"""

# Notes:
"""
1. set.difference()
   Ref: https://www.geeksforgeeks.org/python-set-difference/
"""

# Code:
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
def filterSame(set1, set2):
  # S1: Using for loop
  """
  results = set()
  for i in set1:
    if i not in set2:
      results.add(i)
      print(results)
  return results
  """

  # S2: Using .difference()
  return set1.difference(set2)

print(filterSame(color_list_1, color_list_2))


# Testing:
""" 
"""

