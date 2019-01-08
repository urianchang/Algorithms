# https://www.hackerrank.com/challenges/re-start-re-end/problem
"""
start() & end()
These expressions return the indices of the start and end of the substring
matched by the group
"""
import re

S = raw_input().strip()
k = raw_input().strip()

matches = list(re.finditer(r'(?={})'.format(k), S))
if not matches:
    print "(-1, -1)"
else:
    for m in matches:
        print "({}, {})".format(m.start(), (m.start()+len(k)-1))
