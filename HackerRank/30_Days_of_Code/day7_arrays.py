"""
Day 7: Arrays

Given an array 'A' of 'N' integers, print A's elements
in reverse order as a single line of space-separated numbers.
"""

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
arrString = ""
count = len(arr) - 1
while count >= 0:
    arrString += str(arr[count]) + " "
    count -= 1
print arrString
