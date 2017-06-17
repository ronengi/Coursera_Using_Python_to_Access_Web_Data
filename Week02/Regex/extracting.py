#!/usr/bin/python

import re

# hand = open('regex_sum_42.txt')
hand = open('regex_sum_323544.txt')
sumAll = 0
for line in hand:
    matches = re.findall('[0-9]+', line)
    for num in matches:
        sumAll += int(num)
print(sumAll)

"""
# short version:

import re
print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# List comprehension is mentioned in Chapter 10 and the read() method is covered in Chapter 7.

"""

