# Python 3.7
# https://www.hackerrank.com/challenges/most-commons/problem
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    from collections import Counter

    # Sort string list before putting into Counter to maintain alphabetical
    # order since dictionaries in Python 3 are sorted by when key is added
    s = sorted(input().strip())
    for pair in Counter(s).most_common(3):
        print(*pair)

