# https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re

pattern = r"(\+|-|\.)?\d*\.\d{1,}$"
for _ in range(int(raw_input().strip())):
    N = raw_input().strip()
    print "True" if re.match(pattern, N) else "False"
