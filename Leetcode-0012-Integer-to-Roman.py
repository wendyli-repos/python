# 12. Integer to Roman(https://leetcode.com/problems/integer-to-roman/)
# Question: Given an integer, convert it to a roman numeral.

# Solution: https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php

# Ideas:
""" Get num divided by roman units, starting from the largest, till result is less than or euqal to 0; 
and save correspondence syb.  """

# Steps:
""" 1. let num conduct floor division with each roman unit (starting from the larges);
2. pass the result as a arg to range(). If range(0), the for loop will return nothing and exit the for loop;
3. outside for loop, i will inceare by 1;
4. num is still larger than 0, so still inside while loop
5. repeat for loop for second time, and on; till the reulst of num // val[i] is equal or larger than 1;
6. append correspondence syb to roman_num string;
7. deduct the correspondence val[i] and repeat for loop;
8. until num is euqal or less than 0.  """

# Notes:
# 1. Roman Numeral ranges from 1 to 3,999,999.

class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

#  Testing:
""" convert = Solution()
result = convert.intToRoman(4)
print(result) """

