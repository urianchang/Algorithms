"""
Big Sorting:

Consider an array of numeric strings, 'unsorted', where each
string is a positive number with anywhere from 1 to 10^6 digits.
Sort the array's elements in non-decreasing (i.e. ascending) order
of their real-world integer values and print each element of the
sorted array on a new line.
"""

import sys

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
unsorted.sort(key=int)
for el in unsorted:
    print el
