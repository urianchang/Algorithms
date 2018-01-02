"""
List Comprehensions

URL: https://www.hackerrank.com/challenges/list-comprehensions/problem
"""

x = int(raw_input().strip())
y = int(raw_input().strip())
z = int(raw_input().strip())
n = int(raw_input().strip())

print [ [i, j, k] for i in xrange(x+1) for j in xrange(y+1) for k in xrange(z+1) if ((i+j+k) != n)]
