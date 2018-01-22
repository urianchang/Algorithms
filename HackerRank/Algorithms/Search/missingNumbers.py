"""
Missing Numbers

URL: https://www.hackerrank.com/challenges/missing-numbers/problem
"""

import sys

def missingNumbers(arr, brr):
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    m = int(raw_input().strip())
    brr = map(int, raw_input().strip().split(' '))
    result = missingNumbers(arr, brr)
    print " ".join(map(str, result))
