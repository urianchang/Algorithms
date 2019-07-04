# Python 3
# https://www.hackerrank.com/challenges/python-sort-sort/problem

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    s = sorted(arr, key=lambda a: a[k])
    for l in s:
        print(*l, sep=" ")
