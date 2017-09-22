"""
Quicksort I - Partition

Choose some pivot element, 'p', and partition your unsorted array, 'ar',
into three smaller arrays: 'left', 'right', and 'equal', where each element
in left < p, each element in right > p, and each element in equal = p.

NOTE: There is no need to sort the elements in-place; you can create two lists
and stitch them together at the end.
"""

def partition(ar):
    left = []
    right = []
    equal = []
    p = ar[0]
    for val in ar:
        if val == p:
            equal.append(val)
        elif val < p:
            left.append(val)
        else:
            right.append(val)
    print ' '.join(str(el) for el in (left + equal + right))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)

"""
Sample input:
5
4 5 3 7 2

Sample output:
3 2 4 5 7
"""
