"""
Maximum Perimeter Triangle

URL: https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
"""
n = int(raw_input().strip())    # number of sticks
l = sorted(map(int, raw_input().strip().split()))   # stick lengths

idx = n-3
while idx >= 0 and (l[idx] + l[idx+1] <= l[idx+2]):
    idx -= 1

if idx >= 0:
    print l[idx],l[idx+1],l[idx+2]
else:
    print -1
