# 49. Write a Python program to list all files in a directory in Python.
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-49.php

# Ideas:
"""
1. from os import listdir
2. from os.path import isfile, join
"""

# Steps:
"""  
"""

# Notes:
"""
1. Ref: https://stackoverflow.com/questions/10937806/oserror-error-1-operation-not-permitted
"""

# Code:
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir("/Users/w/Downloads") if isfile(join("/Users/w/Downloads", f))]
# print(files_list)

from os import listdir
files_list = [f for f in listdir("/Users/w/Downloads")]
print(files_list)

# Testing:
""" 
"""

