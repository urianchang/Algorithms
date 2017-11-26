"""
Sherlock and Array

HackerRank url: https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""

for _ in xrange(int(raw_input().strip())):
    n = int(raw_input().strip())    # number of elements
    A = map(int, raw_input().strip().split())   # Array
    total = sum(A)
    running_total = 0
    isBalanced = False
    for num in A:
        if running_total == (total-(running_total+num)):
            isBalanced = True
            break
        running_total += num
    print "YES" if isBalanced else "NO"

"""
Input:
3
1 2 3
4
1 2 3 3

Output:
NO
YES
"""
