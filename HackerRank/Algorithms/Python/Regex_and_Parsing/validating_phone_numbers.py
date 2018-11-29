# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

pattern = r"[789]\d{9}$"
regex = re.compile(pattern)

for _ in range(int(raw_input().strip())):
    N = raw_input().strip()
    print("YES" if regex.match(N) else "NO")
