# https://www.hackerrank.com/challenges/py-set-difference-operation/problem

n = int(raw_input().strip())
roll_n = set(map(int, raw_input().strip().split()))
b = int(raw_input().strip())
roll_b = set(map(int, raw_input().strip().split()))
print len(roll_n.difference(roll_b))
