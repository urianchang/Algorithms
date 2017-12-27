"""
Priyanka and Toys

URL: https://www.hackerrank.com/challenges/priyanka-and-toys/problem
"""

N = int(raw_input().strip())    # Number of toys
w = sorted(map(int, raw_input().strip().split()))   # Weight list

p = w[0] + 4
count = 1
for weight in w:
    if weight > p:
        count += 1
        p = weight+4

print count
