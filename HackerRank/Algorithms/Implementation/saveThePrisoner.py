# https://www.hackerrank.com/challenges/save-the-prisoner/problem

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    s_idx = s - 1   # index of position (0...n-1)
    m_idx = m - 1   # First prisoner gives away candy
    pos = (s_idx + m_idx) % n
    return pos + 1  # position should be (1...n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        # Number of prisoners
        n = int(nms[0])

        # Number of sweets
        m = int(nms[1])

        # Chair number to start passing out treats
        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()