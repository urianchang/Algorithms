"""
Insertion Sort - Part II

In this challenge, don't print every time you move an element.
Instead, print the array after each iteration of the insertion-sort
(i.e. whenever the next element is placed at its correct position).
"""

def insertionSort(ar):
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)

"""
Sample Input:
6
1 4 3 5 6 2

Sample Output:
1 4 3 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 3 4 5 6 2
1 2 3 4 5 6 
"""
