"""
Divisible Sum Pairs:

You are given an array of n integers, A, and a positive integer, k.
Find and print the number of (i, j) pairs where i < j and a[i] + a[j]
is divisible by k.
"""

n, k = map(int, raw_input().strip().split())
a = map(int, raw_input().strip().split())
c = 0

for i in xrange(len(a)):
    for j in xrange(i+1, len(a)):
        if (a[i] + a[j])%k == 0:
            c += 1

print c

"""
Sample Input:
6 3
1 3 2 6 1 2

Sample Output:
5
"""
