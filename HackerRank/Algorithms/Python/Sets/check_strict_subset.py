# https://www.hackerrank.com/challenges/py-check-strict-superset/problem

A = set(map(int, raw_input().strip().split()))

otherSets = []

for _ in range(int(raw_input().strip())):
    otherSets.append(set(map(int, raw_input().strip().split())))

print all([s.issubset(A) for s in otherSets])
