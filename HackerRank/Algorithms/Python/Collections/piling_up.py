# Python 3.7
# https://www.hackerrank.com/challenges/piling-up/problem

for _ in range(int(input())):
    n = int(input())
    sideLengths = list(map(int, input().strip().split()))
    l = len(sideLengths)
    i = 0
    # Lengths have to look like a mountain
    # From left to middle, the numbers should be increasing
    while (i < l - 1) and (sideLengths[i] >= sideLengths[i+1]):
        i += 1

    # From middle to right, the numbers should be decreasing
    while (i < l - 1) and (sideLengths[i] <= sideLengths[i+1]):
        i += 1

    print("Yes" if i == l - 1 else "No")
