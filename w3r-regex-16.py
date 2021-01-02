# 16. Write a Python program to remove leading zeros from an IP(V4) address.
# Question: 
# Input: "216.08.094.196"
# Output: 216.8.94.196 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-16.php
# Ideas:
"""
1. re.sub() to replace one or many matches with a string  
"""

# Steps:
"""  
1. 
"""

# Notes:
"""
1. (Maybe) best practice to using regex is to define patterns first
   Then apply .search(patterns. text) to get result
"""

# Code:
from timer import Timer

import re

@Timer.timer
def remove_zeros_in_ip_address(ip):
  # remove the first zero from the ip & save the rest
  first_zero_pat = "^[0]"
  first_zero_removed_ip = re.sub(first_zero_pat, "", ip)

  # remove other leading zeros after the "."
  leading_zeros_pat = "\.[0]*"
  cleaned_ip = re.sub(leading_zeros_pat, ".", first_zero_removed_ip)

  return cleaned_ip

# Testing:
print(remove_zeros_in_ip_address("216.08.094.196"))
print(remove_zeros_in_ip_address("012.0222.0103.051"))
