"""
Migratory Birds:

A flock of n birds flying across the continent. Each bird has a type,
and the different types are designated by the ID numbers 1, 2, 3, 4,
and 5.

Given an array of n integers where each integer describes the type of a
bird in the flock, find and print the type number of the most common
bird. If two or more types of birds are equally common, choose the
type with the smallest ID number.
"""

counts = [0]*6
n = int(raw_input().strip())
flock = map(int, raw_input().strip().split())

for bird in flock:
    counts[bird] += 1

print counts.index(max(counts))

"""
Sample Input:
6
1 4 4 4 5 3

Sample Output:
4
"""
