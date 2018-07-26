# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter
# A counter is a container that stores elements as
# dictionary keys, and their counts are stored as
# dictionary values.

x = int(raw_input().strip())
sizes = Counter(map(int, raw_input().strip().split()))
N = int(raw_input().strip())

money_earned = 0

for _ in range(N):
    size, paid = map(int, raw_input().strip().split())
    if size in sizes and sizes[size] > 0:
        sizes[size] = sizes[size] - 1
        money_earned += paid

print money_earned
