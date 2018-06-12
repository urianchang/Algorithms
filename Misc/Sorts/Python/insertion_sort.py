# Python 2.7
from utils import timer


def insertionSort(arr):
    # type: (list) -> None
    for i in range(1, len(arr)):
        cur_val = arr[i]
        pos = i-1

        while pos >= 0 and cur_val < arr[pos]:
            arr[pos + 1] = arr[pos]
            pos -= 1

        arr[pos + 1] = cur_val


ex1 = [2, 1, 4, 5, 7, 1, 3, 9, 9, 2]
ex2 = [9, 5, 6, 3, 2, 8, 1, 7, 10, 4]
ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for ts in (ex1, ex2, ex3, ex4):
    print "Before: %s" % ts

    with timer():
        insertionSort(ts)

    print "After: %s\n" % ts
