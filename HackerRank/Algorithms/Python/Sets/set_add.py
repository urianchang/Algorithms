# https://www.hackerrank.com/challenges/py-set-add/problem

c = set()

for _ in range(int(raw_input().strip())):
    c.add(raw_input().strip())

print len(c)