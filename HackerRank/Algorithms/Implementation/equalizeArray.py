"""
Equalize the Array

Karl has an array of n integers. In one operation, he can delete any element
from the array.

Karl wants all the elements of the array to be equal to one another. To do
this, he must delete zero or more elements from the array. Find and print
the minimum number of deletion operations Karl must perform so that all the
array's elements are equal.
"""

n = int(raw_input().strip())
A = map(int, raw_input().strip().split())
d = {}

# Create dictionary to list values and their count
for e in A:
    if d.get(e):
        d[e] += 1
    else:
        d[e] = 1

maxValue = max(d.values())  # Save maximum value to variable
foundMax = []   # In case any repeat counts are found
operations = 0  # Number of deletion operations

for val in d.values():
    if val != maxValue:
        operations += val
    else:
        foundMax.append(val)

if len(foundMax) == 1:
    print operations
else:
    print operations + (maxValue * (len(foundMax) -1))

"""
Sample Input:
5
3 3 2 1 3

Sample Output:
2
"""
