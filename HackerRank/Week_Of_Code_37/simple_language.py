"""
Simple Language

URL: https://www.hackerrank.com/contests/w37/challenges/simple-language
"""

import os
import sys

#
# Complete the maximumProgramValue function below.
#
def maximumProgramValue(n):
    x = 0
    for _ in xrange(n):
        f, v = raw_input().strip().split()
        if f == "add":
            new_x = x + long(v)
        else:
            new_x = long(v)
        x = new_x if new_x > x else x
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    result = maximumProgramValue(n)

    fptr.write(str(result) + '\n')

    fptr.close()
