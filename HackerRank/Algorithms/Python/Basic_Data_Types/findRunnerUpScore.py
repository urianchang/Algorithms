"""
Find the Runner-Up Score

URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
"""

n = int(raw_input().strip())
a = map(int, raw_input().strip().split())

print sorted(set(a))[-2]
