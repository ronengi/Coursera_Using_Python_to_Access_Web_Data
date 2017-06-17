#!/usr/bin/python

"""urllib.request — Extensible library for opening URLs:
https://docs.python.org/3/library/urllib.request.html#module-urllib.request
"""
import urllib.request

fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fhand:
    print(line.strip())

