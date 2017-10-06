"""
HackerRank in a String

We say that a string, 's', contains the word 'hackerrank' if a subsequence
of the characters in 's' spell the word 'hackerrank'. For example,
'haacckkerrannkk' does contain 'hackerrank', but 'haacckkerannk' does not (
missing the second 'r'). You must answer 'q' queries, where each query
consists of a string, 's'. For each query, print 'YES' on a new line if 's'
contains 'hackerrank'; otherwise, print 'NO' instead.
"""

import sys

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    master = 'hackerrank'
    start = 0
    for ch in s:
        if ch == master[start]:
            start += 1
        # Break the loop once we get the desired string
        if start == 10:
            break
    if start != 10:
        print "NO"
    else:
        print "YES"

"""
Input:
2
hereiamstackerrank
hackerworld

Output:
YES
NO
"""
