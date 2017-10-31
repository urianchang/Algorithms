"""
Forming a Magic Square

We define a magic square to be an n x n matrix of distinct positive integers
from 1 to n^2 where the sum of any row, column, or diagonal (of length n) is
always equal to the same number (i.e. the magic constant).

Consider a 3x3 matrix, s, of integers in the inclusive range [1, 9]. We can
convert any digit, a, to any other digit, b, in the range [1,9] at cost
abs(a - b).

Given s, convert it into a magic square at minimal cost by changing zero or more
of its digits. Then print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive
range [1, 9].
"""
import sys

# There are 8 ways to make a magic square
MAGICS = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
]

# Get user inputted square
s = []
for s_i in xrange(3):
    s_temp = map(int,raw_input().strip().split(' '))
    s.append(s_temp)

# Compare user square against every combination of magic square
min_total = float('Inf')
for magic in MAGICS:
    total = 0
    for i in xrange(3):
        zipped = zip(magic[i], s[i])
        for group in zipped:
            if group[0] != group[1]:
                total += abs(group[0] - group[1])
    min_total = min(min_total, total)

print min_total
