"""
Beautiful Pairs

URL: https://www.hackerrank.com/challenges/beautiful-pairs/problem
"""

N = int(raw_input().strip())    # Number of elements in A and B
A = map(int, raw_input().strip().split())   # Array A
B = map(int, raw_input().strip().split())   # Array B

diff = 0

for idx in xrange(N):
    for j in xrange(len(B)):
        if A[idx] == B[j]:
            del B[j]
            diff += 1
            break

if diff != N:
    print diff+1
else:
    print diff-1
