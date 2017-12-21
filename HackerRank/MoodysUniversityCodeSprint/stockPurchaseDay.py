"""
Stock Purchase Day

In a stock-market, there is one special product with infinite stocks. Its stock
price is given for n days, where A[i] denotes the price of the stock on the i-th
day. You are given q queries, each denoting a customer who is willing to buy
the stock for price of atmost x. For each customer, find and print the last
possible day that the customer can purchase the stock. If the purchase is not
possible, print -1. 
"""

# Score 21.25/25: Timed out TC #7, 8, 11.

import sys

def stockPurchaseDay(A, xi, n):
    i = n-1
    while i >= 0:
        if A[i] <= xi:
            return i+1
        else:
            i -= 1
    return -1

if __name__ == "__main__":
    n = int(raw_input().strip())    # number of days
    A = map(int, raw_input().strip().split(' '))    # stock price per day
    cheapest = min(A)
    q = int(raw_input().strip())    # total number of customers
    for a0 in xrange(q):
        xi = int(raw_input().strip())   # customer desired price
        result = stockPurchaseDay(A, xi, n) if xi >= cheapest else -1
        print result
