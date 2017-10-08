"""
Kangaroo:

There are two kangaroos on a number line ready to jump in the positive
direction. The first kangaroo starts at location x1 and moves at a rate
of v1 meters per jump. The second kangaroo starts at location x2 and moves
at a rate of v2 meters per jump. Given the starting locations and movement
rates for each kangaroo, can you determine if they'll ever land at the
same location at the same time?
"""

x1, v1, x2, v2 = map(int, raw_input().strip().split())

'''
position = (number of jumps)*(distance per jump) + starting position
K = n*v + x

So if we want to find same position after same number of jumps...
(n*v1) + x1 = (n*v2) + x2
n(v2 - v1) = x1 - x2
n = x1 - x2 / (v2 - v1)

To check if n is an integer...
(x1 - x2) % (v2 - v1) == 0
'''

if v1 >= v2:
    print "NO"
else:
    print "YES" if (x1 - x2) % (v2 - v1) == 0 else "NO"

"""
Input 0:
0 3 4 2

Output 0:
YES

Input 1:
0 2 5 3

Output 1:
NO
"""
