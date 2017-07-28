"""
Sparse Arrays

There is a collection of 'N' strings. Each string's length
is no more than 20 characters. There are also 'Q' queries.
For each query, you are given a string, and you need to find
out how many times this string occurs in the given collection
of 'N' strings.
"""

"""
Input:
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
"""

d = {}

N = int(raw_input().strip())
for i in range(N):
    s = raw_input().strip()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
Q = int(raw_input().strip())
for i in range(Q):
    q = raw_input().strip()
    if q in d:
        print d[q]
    else:
        print 0

"""
Output:
2
1
0
"""
