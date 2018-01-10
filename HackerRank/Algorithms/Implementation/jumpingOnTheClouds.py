"""
Jumping on the Clouds

URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
"""
import sys

def jumpingOnClouds(c):
    i = 0
    j = 0
    while i < len(c) - 2:
        if c[i+2] != 1:
            i += 2
        else:
            i += 1
        j += 1
    if i == len(c) - 2:
        j += 1
    return j

if __name__ == "__main__":
    n = int(raw_input().strip())
    c = map(int, raw_input().strip().split(' '))
    result = jumpingOnClouds(c)
    print result
