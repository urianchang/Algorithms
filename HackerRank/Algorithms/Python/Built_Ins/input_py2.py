# https://www.hackerrank.com/challenges/input/problem

"""
`input()`
In Python 2, the expression `input()` is equivalent to `eval(raw_input(prompt))`
"""

x, k = map(int, raw_input().strip().split())
print input() == k
