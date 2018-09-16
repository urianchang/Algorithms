# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re

for _ in range(int(raw_input().strip())):
    s = raw_input().strip()
    try:
        re.compile(s)
        print "True"
    except re.error:
        print "False"
