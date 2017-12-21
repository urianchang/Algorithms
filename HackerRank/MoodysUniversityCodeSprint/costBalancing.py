"""
Cost Balancing:

Anita and her friends go on a trip. Now, they are back home and need to balance
their expenses. During the trip, they perform many transactions but don't divide
the expenses equally all the time. The total expenses should be balanced in such
a way that everyone pays an equal amount. Given the information about the
transactions, Anita needs to find who owes others and who should get money.

Anita has an ID number of 1 and her friends are represented by IDs from 2 to m.

There will be n transactions, each consisting of a person's ID and the amount of
money that he/she paid. Note that, the required payment for all might be
fractional. To avoid this situation, Anita has decided to pay some extra money
(if needed) so that everybody has to pay a whole amount after that.
"""

# n - number of transactions
# m - number of friends (1 to m)
n, m = map(int, raw_input().strip().split())

# Create dictionary of friends and cost
d = dict(zip(xrange(1, m+1), [0]*(m)))
total = 0

# Iterate through transactions
for _ in xrange(n):
    f, p = map(int, raw_input().strip().split())
    total += p
    d[f] += p

c = total/m
leftover = total - (c*m)

for key, value in d.items():
    if key == 1:
        print key, (d[key] - (c+leftover))
    else:
        print key, (d[key] - c)
