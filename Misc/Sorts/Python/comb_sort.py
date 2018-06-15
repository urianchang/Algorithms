# Python 2.7
from utils import timer


def comb_sort(arr):
    #type: (list) -> None
    gap = len(arr)
    swapping = True
    while swapping or gap >= 1:
        swapping = False
        for i in range(len(arr)-gap):
            if arr[i] > arr[i+gap]:
                swapping = True
                arr[i], arr[i+gap] = arr[i+gap], arr[i]

        # Shrink gap
        gap = (gap*10)/13


ex1 = [2, 1, 4, 5, 7, 1, 3, 9, 9, 2]
ex2 = [9, 5, 6, 3, 2, 8, 1, 7, 10, 4]
ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for ts in (ex1, ex2, ex3, ex4):
    print "Before: %s" % ts

    with timer():
        comb_sort(ts)

    print "After: %s\n" % ts
