"""
Jumping on the Clouds - Revisited

URL: https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
"""
import sys

def jumpingOnClouds(c, k):
    i = k%len(c)
    e = 100 - (c[i] * 2 + 1)
    while i != 0:
        i = (i+k)%len(c)
        e -= c[i] * 2 + 1
    return e

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')   # Number of clouds and jump distance
    n, k = [int(n), int(k)]
    c = map(int, raw_input().strip().split(' '))
    result = jumpingOnClouds(c, k)
    print result
