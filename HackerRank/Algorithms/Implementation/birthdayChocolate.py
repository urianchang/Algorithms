"""
Birthday Chocolate:

Lily has a chocolate bar consisting of a row of 'n' squares where
each square has an integer written on it. She wants to share it
with Ron for his birthday, which falls on month m and day d. Lily
wants to give Ron a piece of chocolate only if it contains m
consecutive squares whose integers sum to d.
"""

n = int(raw_input().strip())
s = map(int, raw_input().strip().split())
d, m = map(int, raw_input().strip().split())

count = 0
for i in xrange(n-m+1): # Add 1 because n has minimum of 1
    if d == sum(s[i:i+m]):
        count += 1

print count

"""
Input0:
5
1 2 1 3 2
3 2

Output0:
2

Input1:
6
1 1 1 1 1 1
3 2

Output1:
0

Input2:
1
4
4 1

Output2:
1
"""
