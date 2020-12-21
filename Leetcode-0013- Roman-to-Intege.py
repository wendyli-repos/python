# 13. Roman to Integer(https://leetcode.com/problems/roman-to-integer/)
## Question: 
Given a roman numeral, convert it to an integer.

## Solution:
Reference: https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-2.php
```py
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
```

## Ideas:
to be edited. 

## Steps:
1. to be edited.

## Notes:
1. 'IV', 'IV', 'XL', 'XC', 'CD', CM'

