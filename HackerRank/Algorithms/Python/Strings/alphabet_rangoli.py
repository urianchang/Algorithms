# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
import string


ALPHA = string.ascii_lowercase

def print_rangoli(size):
    for i in range(size - 1, 0, -1):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = ALPHA[j + i]
            row[size - 1 + j] = ALPHA[j + i]
        print("-".join(row))

    for i in range(0, size):
        row = ["-"] * (size * 2 - 1)
        for j in range(0, size - i):
            row[size - 1 - j] = ALPHA[j + i]
            row[size - 1 + j] = ALPHA[j + i]
        print("-".join(row))

print_rangoli(3)

"""
Expected:

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
