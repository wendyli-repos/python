# 11. Write a Python program that matches a word at the end of string, with optional punctuation.
# Question: 
# Input: 
# Output: 
# Solution: https://www.w3resource.com/python-exercises/re/python-re-exercise-11.php
# Ideas:
"""
1. \w
2. +
3. \S
4. *
5. $
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
def end_with_a_word_and_optional_punc(string):
  patterns = "\w+\S*$"
  x = re.search(patterns, string)
  if x:
    return f'Found a match!, {x.group()}'
  else:
    return f'Not matched!'

# Testing:
print(end_with_a_word_and_optional_punc("The quick brown fox jumps over the lazy dog."))
print(end_with_a_word_and_optional_punc("The quick brown fox jumps over the lazy dog. "))
print(end_with_a_word_and_optional_punc("The quick brown fox jumps over the lazy dog "))
