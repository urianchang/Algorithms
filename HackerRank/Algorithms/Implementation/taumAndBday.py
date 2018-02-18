"""
Taum and B'day

URL: https://www.hackerrank.com/challenges/taum-and-bday/problem
"""

for _ in xrange(int(raw_input().strip())):
    B, W = map(int, raw_input().strip().split())
    X, Y, Z = map(int, raw_input().strip().split())
    print min(X, Y+Z)*B + min(Y, X+Z)*W
