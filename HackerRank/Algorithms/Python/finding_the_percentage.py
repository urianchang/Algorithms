"""
Finding the percentage

URL: https://www.hackerrank.com/challenges/finding-the-percentage/problem
"""
s = {}
for _ in xrange(int(raw_input().strip())):
    l = raw_input().strip().split()
    s[l[0]] = "{:0.2f}".format((sum([float(i) for i in l[1:]]) / 3.0))
print s[raw_input().strip()]
