"""
Bon Appetit

Anna and Brian order 'n' items at a restaurant, but Anna declines to eat any
of the k-th item due to an allergy. When the check comes, they decided to
split the cost of all the items they shared; however, Brian may have
forgotten that they didn't split the k-th item and accidentally charged
Anna for it.

You are given n, k, the cost of each of the n items, and the total amount
of money that Brian charged Anna for her portion of the bill. If the bill
is fairly split, print 'Bon Appetit'; otherwise, print the amount of money
that Brian must refund to Anna.
"""

import sys

def bonAppetit(n, k, dishes, charged):
    expectedBill = 0
    for i in xrange(n):
        if i != k:
            expectedBill += dishes[i]
    expectedShare = expectedBill/2
    return charged - expectedShare if expectedShare != charged else "Bon Appetit"

n, k = map(int, raw_input().strip().split())
dishes = map(int, raw_input().strip().split())
charged = int(raw_input().strip())

print bonAppetit(n, k, dishes, charged)

"""
Sample Input 0:
4 1
3 10 2 9
12

Sample Output 0:
5

Sample Input 1:
4 1
3 10 2 9
7

Sample Output 1:
Bon Appetit
"""
