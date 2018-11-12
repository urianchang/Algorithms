# https://www.hackerrank.com/challenges/py-check-subset/problem

for _ in range(int(raw_input().strip())):
    len_A = int(raw_input().strip())
    A = set(map(int, raw_input().strip().split()))
    len_B = int(raw_input().strip())
    B = set(map(int, raw_input().strip().split()))
    print A.issubset(B)
