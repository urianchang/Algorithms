"""
Buy Maximum Stocks

In a stock market, there is a product with its infinite stocks.
The stock prices are given for 'n' days, where arr[i] denotes the
price of the stock on the i-th day. There is a rule that a customer
can buy at most i stock on the i-th day. If the customer has an
amount of 'k' dollars initially, find out the maximum number of
stocks they can buy.
"""

import sys

def buyMaximumProducts(n, k, a):
    

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    k = long(raw_input().strip())
    result = buyMaximumProducts(n, k, arr)
    print result
