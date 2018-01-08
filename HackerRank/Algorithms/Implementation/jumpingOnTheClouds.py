"""
Jumping on the Clouds

URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""

import sys

def jumpingOnClouds(c):
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    result = jumpingOnClouds(c)
    print result
