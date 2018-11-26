# https://www.hackerrank.com/challenges/hex-color-code/problem
import re

pattern = r"(?<!^)#[0-9A-Fa-f]{3,6}"    # does not match start of the line
hexes = []
for _ in range(int(raw_input().strip())):
    code = raw_input().strip()
    hexes.extend(re.findall(pattern, code))

for hex in hexes:
    print hex
