"""
Service Lane

URL: https://www.hackerrank.com/challenges/service-lane/problem
"""

N, T = map(int, raw_input().strip().split())
width = map(int, raw_input().strip().split())

for _ in xrange(T):
    i, j = map(int, raw_input().strip().split())
    print min(width[i:j+1])
