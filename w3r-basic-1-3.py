# 3. Return Current Date and Time
# Question: Write a Python program to display the current date and time.
# Input:
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

# Ideas:
"""
1. import datetime module
2. .now()   
"""

# Steps:
"""  
"""

# Notes:
"""
1. Roman Numeral ranges from 1 to 3,999,999.
"""

# Code:
import datetime
x = datetime.datetime.now()
print("Current date and time: ")
print(x.strftime("%d-%m-%Y"))
print(x.strftime("%d %B, %Y"))
        

# Testing:
""" 
convert = Solution()
result = convert.intToRoman(4)
print(result) 
"""

