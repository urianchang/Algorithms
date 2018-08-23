# Python 2.7
from utils import timer


def counting_sort(arr):
    #type: (list) -> list
    # Create count list
    max_val = max(arr)
    count_arr = [0 for _ in range(max_val+1)]
    output = [0 for _ in range(len(arr))]
    for val in arr:
        count_arr[val] += 1
    # print count_arr

    # Add up the counts
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    # print count_arr

    # Sort based on the count arr
    for val in arr:
        pos = count_arr[val] - 1
        output[pos] = val
        count_arr[val] -= 1

    return output


ex1 = [2, 1, 4, 5, 7, 1, 3, 9, 9, 2]
ex2 = [9, 5, 6, 3, 2, 8, 1, 7, 10, 4]
ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for ts in (ex1, ex2, ex3, ex4):
    print "Before: %s" % ts

    with timer():
        ts = counting_sort(ts)

    print "After: %s\n" % ts
