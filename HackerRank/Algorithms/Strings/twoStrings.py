"""
Two Strings:

Given two strings, a and b, determine if they share a substring.

Constraints:
    * 1 <= p <= 10
    * 1 <= a, b <= 10^5
"""

p = int(raw_input().strip())

for _ in xrange(p):
    # Only need to check if there is a common character from each word
    a = set(raw_input().strip())
    b = set(raw_input().strip())
    print "YES" if a.intersection(b) else "NO"

"""
Input:
2
hello
world
hi
world

Output:
YES
NO
"""
