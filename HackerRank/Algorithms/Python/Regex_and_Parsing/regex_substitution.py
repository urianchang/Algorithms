# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re


def parsing_and_or(match):
    chars = match.group(0)
    if chars == "&&":
        return "and"
    elif chars == "||":
        return "or"
    else:
        return chars


for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', parsing_and_or, input()))
