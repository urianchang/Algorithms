# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms
#!/bin/python3

import math
import os
import random
import re
import sys


def maxMin(k, arr):
    arr.sort()
    return min([
        abs(arr[i+k-1] - arr[i]) 
        for i in range(len(arr)-k+1)
    ])


assert maxMin(3, [10, 100, 300, 200, 1000, 20, 30]) == 20
assert maxMin(4, [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]) == 3
assert maxMin(2, [1, 2, 1, 2, 1]) == 0
