"""
Find Digits:

Given an integer, N, traverse its digits and determine how many digits
evenly divide N. Print the number of evenly divisible digits.

Each digit is considered to be unique, so each occurrence of the same evenly
divisible digit should be counted (i.e. for N=111, the answer is 3).
"""

T = int(raw_input().strip())

for _ in xrange(T):
    N = raw_input().strip()
    c = 0
    for n in N:
        if n == "0":
            continue
        if int(N)%int(n) == 0:
            c += 1
    print c

"""
Input:
2
12
1012

Output:
2
3
"""
