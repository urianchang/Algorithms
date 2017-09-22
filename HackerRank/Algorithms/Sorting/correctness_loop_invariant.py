"""
Correctness and the Loop Invariant

In the InsertionSort code below, there is an error. Can you fix it? Print the
array only once, when it is fully sorted.
"""

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        # Set j to be greater than or equal to 0
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))

"""
Sample input:
6
1 4 3 5 6 2

Sample output:
1 2 3 4 5 6
"""
