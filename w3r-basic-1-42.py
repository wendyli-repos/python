# 42. Write a Python program to determine whether a Python shell is executing in 32bit or 64bit mode on OS?
# Question: 
# Input: 
# Output:
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-42.php

# Ideas:
"""
1. import struct
2. struct.calcsize()
3. "P" represents void * (a generic pointer). On 32-bit systems a pointer is 4 bytes, and on a 64-bit system a pointer requires 8 bytes. 
"""

# Steps:
"""  
"""

# Notes:
"""
1. Ref: https://stackoverflow.com/questions/27816562/what-does-struct-calcsizep-exactly-mean
"""

# Code:
import struct
print(struct.calcsize("P") * 8)



# Testing:
""" 
"""

