"""
Fraudulent Activity Notifications:

HackerLand National Bank has a simple policy for warning clients about
possible fraudulent account activity. If the amount spent by a client
on a particular day is greater than or equal to 2x the client's median
spending for the last d days, they send the client a notification about
potential fraud. The bank doesn't send the client any notifications until
they have at least d prior days of transaction data.

Given the value of d and a client's total daily expenditures for a period
of n days, find and print the number of times the client will receivie a
notification over all n days.

NOTE: The median of a list of numbers can be found by arranging all the
numbers from smallest to greatest. If there is an odd number of numbers,
the middle one is picked. If there is an even number of numbers, median
is then defined to be the average of the two middle values.
"""

n, d = map(int, raw_input().strip().split())
expenses = map(int, raw_input().strip().split())
notifications = 0

for i in xrange(len(expenses)):
    if i < d:
        continue
    if i == d:
        data_unsorted = expenses[ i-d : i ]
        data = sorted(data_unsorted)
    if i > d:
        data_unsorted.pop(0)
        data_unsorted.append(expenses[i])
        data = sorted(data_unsorted)
    # Find median of transaction history
    if d%2 == 0:    # Check if d is even
        median = (data[int(d/2)] + data[int(d/2) - 1]) / 2.0
    else:
        median = data[int(d/2)]
    if expenses[i] >= 2*(median):
        notifications += 1

print notifications

"""
Sample Input 0:
9 5
2 3 4 2 3 6 8 4 5

Sample Output 0:
2

Sample Input 1:
5 4
1 2 3 4 4

Sample Output 1:
0
"""
