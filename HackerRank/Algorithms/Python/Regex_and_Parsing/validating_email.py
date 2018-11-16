# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem

import re

pattern = r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>"
for _ in range(int(raw_input().strip())):
    n, e = raw_input().strip().split()
    res = re.match(pattern, e)
    if res:
        print n, e
