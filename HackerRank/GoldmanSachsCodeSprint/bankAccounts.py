'''
Bank Accounts:

You are going to receive 'n' payments in the upcoming month.
Payments are numbered from 0 to n - 1 and p determines the
amount of money in dollars that will be paid in connection
with the i-th payment. Before receiving the payments, you
have two banking options to consider:
    1. You can receive all the payments on your current bank
        account remembering that the bank charges you for each
        payment i max(k, x% of p), where k and x are given.
    2. You can pay the bank d dollars upfront to open a new special
        account for which the bank doesn't charge you for any
        upcoming transactions.

Decide which of the above two options is more profitable to you.
If both ways are equally profitable, then you prefer to be charged
for each transaction.
'''

import sys

def feeOrUpfront(n, k, x, d, p):
    feeOption = 0
    for i in xrange(n):
        feeOption += max(k, ((x/100.0)*p[i]))
    if feeOption <= d:
        return "fee"
    else:
        return "upfront"

if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        n, k, x, d = raw_input().strip().split(' ')
        n, k, x, d = [int(n), int(k), int(x), int(d)]
        p = map(int, raw_input().strip().split(' '))
        result = feeOrUpfront(n, k, x, d, p)
        print result
