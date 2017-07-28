"""
Left Rotation

A 'left rotation' on an array of size 'n' shifts each
of the array's elements 1 unit to the left. For example,
if 2 left rotations are performed on array [1, 2, 3, 4, 5],
then the array would become [3, 4, 5, 1, 2].

Given an array of 'n' integers and a number 'd', perform 'd'
left rotations on the array. Then print the updated array as
a single line of space-separated integers.
"""

n, d = map(int, raw_input().strip().split())
arr = map(int,raw_input().strip().split(' '))
arr = arr[d:] + arr[0:d]
print ' '.join(map(str, arr))
