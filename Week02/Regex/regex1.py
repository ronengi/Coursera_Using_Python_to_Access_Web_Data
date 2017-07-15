#!/usr/bin/python

import re


hand = open('../../file1.text')
for line in hand:
    line = line.rstrip()
    if re.search('^xdg', line):     # <==> if line.startswith('xdg'):
        print(line)


print()

x = 'My 2 favorite numbers are 43, 34 and 44'
y = re.findall('[0-9]+', x)
print(y)

print()

s1 = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
print(re.findall('\S+?@\S+', s1))

print()

