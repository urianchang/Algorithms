"""
Sherlock and Array

HackerRank url: https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""

for _ in xrange(int(raw_input().strip())):
    n = int(raw_input().strip())    # number of elements
    A = map(int, raw_input().strip().split())   # Array
    isBalanced = False
    for i in xrange(n):
        if sum(A[:i]) == sum(A[i+1:]):
            isBalanced = True
    print "YES" if isBalanced else "NO"
