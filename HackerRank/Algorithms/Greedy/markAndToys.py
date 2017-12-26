"""
Mark and Toys

URL: https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

n, k = map(int, raw_input().strip().split())    # Number of toys and money
l = sorted(map(int, raw_input().strip().split()))   # Toy prices

count = 0
for price in l:
    if k >= price:
        count += 1
        k -= price
    if k < price:
        break

print count
