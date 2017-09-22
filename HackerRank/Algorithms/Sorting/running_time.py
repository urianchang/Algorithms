"""
Running Time of Algorithms

Can you modify your previous Insertion Sort implementation to keep track of the
number of shifts it makes while sorting? The only thing you should print is the
number of shifts made by the algorithm to completely sort the array. A shift
occurs when an element's position changes in the array. Do not shift an element
if it is not necessary.
"""

def insertion_sort(l):
    c = 0
    for i in xrange(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           c += 1
        l[j+1] = key
    print c

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)

"""
Sample input:
5
2 1 3 1 2

Sample output:
4
"""
