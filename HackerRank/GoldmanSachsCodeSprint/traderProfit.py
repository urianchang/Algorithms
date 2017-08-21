"""
Trader Profit:

Mike is a stock trader and makes a profit by buying and selling stocks.
He buys a stock at a lower price and sells it at a higher price to book
a profit. He has come to know the stock prices of a particular stock for
'n' upcoming days in future and wants to calculate the maximum profit
by doing the right transactions (single transaction = buying + selling).
Can you help him maximize his profit?

NOTE: A transaction starts after the previous transaction has ended. Two
transactions can't overlap or run in parallel.

The stock prices are given in the form of an array A for n days.

Given the stock prices and a positive integer k, find and print the maximum
profit Mike can make in at most k transactions.
"""

import sys

def traderProfit(k, n, A):
    # Complete the function below

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        k = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = traderProfit(k, n, arr)
        print result
