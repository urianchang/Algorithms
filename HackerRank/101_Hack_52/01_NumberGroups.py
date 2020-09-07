# https://www.hackerrank.com/contests/101hack52/challenges/number-groups
import math
import os
import random
import re
import sys


def sumOfGroup(k: int) -> int:
    # Return the sum of the elements of the k'th group.
    return pow(k, 3)


# (1)
assert sumOfGroup(1) == 1
# (3, 5)
assert sumOfGroup(2) == 8
# (7, 9, 11)
assert sumOfGroup(3) == 27
# (13, 15, 17, 19)
assert sumOfGroup(4) == 64