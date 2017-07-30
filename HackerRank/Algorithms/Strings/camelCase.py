"""
Camel Case:

Alice wrote a sequence of words in CamelCase as a string of letters 's',
having the properties:
    * It's a concatenation of one or more words consisting of English letters
    * All letters in the first word are lowercase
    * For each of the subsequent words, the first letter is uppercase
        and rest of the letters are lowercase

Given 's', print the number of words in s on a new line.
"""

import sys

s = raw_input().strip()
c = 1
for i in range(len(s)):
    if s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        c += 1
print c
