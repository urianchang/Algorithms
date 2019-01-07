# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""
findall()
The expression re.findall() returns all the non-overlapping matches of patterns
in a string as a list of strings

finditer()
The expression re.finditer() returns an iterator yielding MatchObject instances
over all non-overlapping matches for the re pattern in the string
"""
import re

# Substrings that contain 2+ vowels and must lie in between 2 consonants
pattern = r'(?<=[^aeiouAEIOU]){1}([aeiouAEIOU]{2,})(?=[^aeiouAEIOU]){1}'

S = raw_input().strip()
matches = re.findall(pattern, S)
print('\n'.join(matches) if matches else -1)

"""
Sample input:
rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample output:
ee
Ioo
Oeo
eeeee
"""
