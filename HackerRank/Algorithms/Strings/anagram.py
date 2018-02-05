"""
Anagram

URL: https://www.hackerrank.com/challenges/anagram/problem
"""

import sys

def anagram(s):
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagaram(s)
    print(result)
