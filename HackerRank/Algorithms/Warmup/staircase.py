"""
Staircase

Write a program that prints a staircase of size n.
"""

#!/bin/python

import sys


n = int(raw_input().strip())
for num in range(n):
    str = ""
    str += " "*(n-1-num)
    str += "#"*(1 + num)
    print str
