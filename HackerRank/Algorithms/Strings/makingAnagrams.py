"""
Making Anagrams:

Given two strings, a and b, that may or may not be of 
the same length, determine the minimum number of 
character deletions required to make a and b anagrams.
Any characters can be deleted from either or the strings. 
"""
import sys
from collections import Counter 

def makingAnagrams(a, b):
    ca = Counter(a)
    cb = Counter(b)
    ca.subtract(cb)
    return sum(abs(x) for x in ca.values())

a = raw_input().strip()
b = raw_input().strip()
result = makingAnagrams(a, b)
print(result)