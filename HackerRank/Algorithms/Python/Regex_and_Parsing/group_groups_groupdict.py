# https://www.hackerrank.com/challenges/re-group-groups/problem
"""
group()
A group() expression returns one or more subgroups of the match

groups()
A groups() expression returns a tuple containing all the subgroups of the match

groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups
of the match, keyed by the subgroup name
"""
import re

# Capture the last alphanumeric character
pattern = r'([a-zA-Z0-9])\1+'

S = raw_input().strip()
matches = re.search(pattern, S)
print(matches.group(1) if matches else -1)
