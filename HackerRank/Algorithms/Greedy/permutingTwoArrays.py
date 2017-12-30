"""
Permuting Two Arrays

URL: https://www.hackerrank.com/challenges/two-arrays/problem
"""

for _ in xrange(int(raw_input().strip())):
    n, k = map(int, raw_input().strip().split())
    A = map(int, raw_input().strip().split())
    B = map(int, raw_input().strip().split())
    A.sort(reverse=True)
    B.sort(reverse=False)
    is_valid = True
    for i in xrange(n):
        if A[i] + B[i] < k:
            is_valid = False
    print "YES" if is_valid else "NO"
