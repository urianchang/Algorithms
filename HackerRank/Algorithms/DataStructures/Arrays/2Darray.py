"""
2D Array - DS

Given a 6x6 2D array, calculate the hourglass sum
for every hourglass in array, and then print the
maximum hourglass sum.
"""

import sys

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

sumArr = []
for i in range(4):
    for idx in range(4):
        curSum = 0
        curSum += arr[i][idx] + arr[i][idx+1] + arr[i][idx+2]
        curSum += arr[i+1][idx+1]
        curSum += arr[i+2][idx] + arr[i+2][idx+1] + arr[i+2][idx+2]
        sumArr.append(curSum)
print max(sumArr)
