"""
Jim and the Orders

URL: https://www.hackerrank.com/challenges/jim-and-the-orders/problem
"""
from operator import itemgetter

orders = []

for i in xrange(int(raw_input().strip())):
    t, d = map(int, raw_input().strip().split())
    orders.append((i+1, t+d))

# Sort based on completion time
orders.sort(key=itemgetter(1))

# Create string to return
order_string = ""
for order in orders:
    order_string += str(order[0]) + " "

print order_string
