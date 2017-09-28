"""
Closest Numbers:

Sorting is often useful as the first step in many different tasks.
The most common task is to make finding things easier, but there
are other uses, as well.

Given a list of unsorted integers, 'A', can you find the pair of
elements that have the smallest absolute different between them?
If there are multiple pairs, find them all.
"""

N = int(raw_input().strip())
A = map(int, raw_input().strip().split())

# Sort the array in ascending order
A = sorted(A)

# Iterate through the array and save lists of smallest difference
n1 = 0
n2 = 1
minDiff = abs(A[n1] - A[n2])
l = []

while n2 < len(A):
    if (A[n2] - A[n1]) < minDiff:
        minDiff = abs(A[n1] - A[n2])
        l = [ [A[n1], A[n2]] ]
    elif (A[n2] - A[n1]) == minDiff:
        l.append([A[n1], A[n2]])
    n1 += 1
    n2 += 1

# Print out list of pairs
s = ""
for i in xrange(len(l)):
    s += str(l[i][0]) + " " + str(l[i][1]) + " "

print s

"""
Sample Input 1:
10
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854

Sample Output 1:
-20 30

Sample Input 2:
12
-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854 -520 -470

Sample Output 2:
-520 -470 -20 30

Sample Input 3:
4
5 4 3 2

Sample Output 3:
2 3 3 4 4 5

"""
