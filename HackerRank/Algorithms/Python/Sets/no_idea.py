# Python 3.7
# https://www.hackerrank.com/challenges/no-idea/problem
n, m = map(lambda x: int(x), input().strip().split())
arr = map(lambda x: int(x), input().strip().split())

a = set(map(lambda x: int(x), input().strip().split()))
b = set(map(lambda x: int(x), input().strip().split()))

happiness = 0
for i in arr:
    happiness += (i in a) - (i in b)
print(happiness)
