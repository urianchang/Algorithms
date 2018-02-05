"""
Anagram

URL: https://www.hackerrank.com/challenges/anagram/problem
"""

import sys

def anagram(s):
    if len(s)%2 != 0:
        return -1
    s1 = list(s[:len(s)/2])
    s2 = list(s[len(s)/2:])
    for letter in s1:
        if letter in s2:
            s2.pop(s2.index(letter))
    return len(s2)

q = int(raw_input().strip())    # Number of TC's
for a0 in xrange(q):
    s = raw_input().strip()
    result = anagram(s)
    print(result)
