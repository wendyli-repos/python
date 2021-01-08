# 14. Write a Python program to calculate number of days between two dates.
# Question: 
# Input: Sample dates : (2014, 7, 2), (2014, 7, 11)
# Output: Expected output : 9 days
# Solution: https://www.w3resource.com/python-exercises/python-basic-exercise-14.php

# Ideas:
"""
1. import datetime
2. datetime.datetime(year, month, day)
3. <class 'datetime.timedelta'>.days
"""

# Steps:
"""  
"""

# Notes:
"""
1. Python datetime module ref: https://www.programiz.com/python-programming/datetime
"""

# Code:
import datetime
date1 = datetime.date(2014, 7, 2)
date2 = datetime.date(2014, 7, 11)
daysBetween = date2 - date1  # returns a instance of class 'timedelta'; has prop .days to return days
print("date1: {}; date2: {}; daysBetween: {} days".format(date1, date2, daysBetween.days))

# Testing:
""" 
"""

