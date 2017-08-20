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
    stocks = 0
    d = {}
    for idx in xrange(len(a)):
        if a[idx] in d:
            d[a[idx]].append(idx + 1)
        else:
            d[a[idx]] = [idx + 1]
    avail = sorted(d.keys())
    for i in xrange(len(avail)):
        if k <= 0 or k <= avail[i]:
            return stocks
        else:
            while d[avail[i]]:
                d[avail[i]].sort()
                maxQuantity = d[avail[i]].pop()
                while (maxQuantity > 0):
                    cost = maxQuantity * avail[i]
                    if k > cost:
                        k -= cost
                        stocks += maxQuantity
                        break
                    else:
                        maxQuantity -= 1
    return stocks

    # a.sort()
    # for i in xrange(len(a)):
    #     if k <= 0 or k <= a[i]:
    #         return stocks
    #     maxQuantity = d[a[i]].pop(d[a[i]].index(max(d[a[i]])))
    #     while (maxQuantity > 0):
    #         cost = maxQuantity * a[i]
    #         if k > cost:
    #             k -= cost
    #             stocks += maxQuantity
    #             break
    #         else:
    #             maxQuantity -= 1
    # return stocks

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    k = long(raw_input().strip())
    result = buyMaximumProducts(n, k, arr)
    print result
