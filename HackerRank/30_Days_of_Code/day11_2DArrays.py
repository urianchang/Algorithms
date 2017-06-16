"""
Day 11: 2D Arrays

Given a 6x6 2D array 'A'. Calculate the hourglass sum for
every hourglass in A, then print the maximum hourglass sum.
"""

import sys

arr = []
for arr_i in xrange(6):
   arr_temp = map(int,raw_input().strip().split(' '))
   arr.append(arr_temp)

sums = []
for i in xrange(4):
    for idx in xrange(4):
        total = arr[i][idx] + arr[i][idx+1] + arr[i][idx+2] # Hourglass row 1
        total += arr[i+1][idx+1]    # Hourglass row 2
        total += arr[i+2][idx] + arr[i+2][idx+1] + arr[i+2][idx+2]  # Hourglass row 3
        sums.append(total)
print max(sums)
