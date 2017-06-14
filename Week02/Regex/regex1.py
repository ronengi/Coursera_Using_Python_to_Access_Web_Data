#!/usr/bin/python

import re


hand = open('../../file1.text')
for line in hand:
    line = line.rstrip()
    if re.search('^xdg', line):
        print(line)

print()

x = 'My 2 favorite numbers are 43, 34 and 44'
y = re.findall('[0-9]+', x)
print(y)

print()

