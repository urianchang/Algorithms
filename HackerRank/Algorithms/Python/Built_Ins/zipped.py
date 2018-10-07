# https://www.hackerrank.com/challenges/zipped/problem

N, X = map(int, raw_input().strip().split())
grades = []

for _ in range(X):
    grades.append(map(float, raw_input().strip().split()))

for s in zip(*grades):
    print "%.1f" % (sum(s)/len(s))
