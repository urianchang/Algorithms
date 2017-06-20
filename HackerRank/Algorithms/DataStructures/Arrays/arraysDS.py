"""
Arrays - DS

Given an array 'A' of 'N' integers, print each
element in reverse order as a single line of
space-separated integers.
"""

import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
string = ""
for i in range(len(arr)):
    string += str(arr.pop()) + " "
print string
