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
import sys
import bisect
'''
Useful reading about bisect...

https://docs.python.org/2/library/bisect.html

TL;DR: This method allows us to insert a value into a sorted array without
        having to resort it.
'''

n, d = map(int, raw_input().strip().split())
expenses = map(int, raw_input().strip().split())
notifications = 0
data = []

# Unused helper function: Counting Sort
def countingSort(a):
    max_val = max(a)
    frequency = [0] * (max_val+1)
    sorts = [0] * len(a)
    for i in xrange(len(a)):
        frequency[a[i]] += 1
    for i in xrange(1, max_val+1):
        frequency[i] += frequency[i-1]
    for i in xrange(len(a)):
        num = a[i]
        sorts[ frequency[num] - 1 ] = num
        frequency[num] -= 1
    return sorts

# Create sorted data set from index 0 to first d
for i in xrange(d):
    # Use bisect to keep data set sorted
    bisect.insort(data, expenses[i])

# Now start from first d to end of data set to check for notifications
for i in xrange(d, n):

    # Find median of transaction history
    if d%2 == 0:    # Check if d is even
        median = (data[int(d/2)] + data[int(d/2) - 1]) / 2.0
    else:
        median = data[int(d/2)]

    # Determine if a notification is necessary
    if expenses[i] >= 2*(median):
        notifications += 1

    # Modify data set: remove oldest value and add new value
    to_remove = bisect.bisect(data, expenses[i - d]) - 1
    data.pop(to_remove)
    bisect.insort(data, expenses[i])

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
