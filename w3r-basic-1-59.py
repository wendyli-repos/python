# 59. Write a Python program to convert height (in feet and inches) to centimeters.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-59.php

# Ideas:
"""
"""

# Steps:
"""  
"""

# Notes:
"""
"""

# Code:
print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Your height is : %d cm." % h_cm)

# Testing:
""" 
"""

