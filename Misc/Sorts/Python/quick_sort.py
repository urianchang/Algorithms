# Python 2.7
from utils import timer


def pivot_on_right(arr, left, right):
    # type: (list, int, int) -> int
    pivot = arr[right]
    pointer = left - 1

    for idx in range(left, right):
        if arr[idx] <= pivot:
            # put to left of pivot
            pointer += 1
            arr[pointer], arr[idx] = arr[idx], arr[pointer]
            # print arr

    end = pointer + 1
    arr[end], arr[right] = arr[right], arr[end]
    return end


def pivot_on_left(arr, left, right):
    # type: (list, int, int) -> int
    pivot = arr[left]
    p_left = left + 1
    p_right = right
    done = False

    while not done:
        while p_left <= p_right and arr[p_left] <= pivot:
            p_left += 1

        while p_right >= p_left and arr[p_right] >= pivot:
            p_right -= 1

        if p_left > p_right:
            done = True
        else:
            arr[p_left], arr[p_right] = arr[p_right], arr[p_left]

    arr[p_right], arr[left] = arr[left], arr[p_right]
    return p_right


def quick_sort(arr, left, right):
    #type: (list, int, int) -> None
    if right > left:
        # p_idx = pivot_on_right(arr, left, right)
        p_idx = pivot_on_left(arr, left, right)
        quick_sort(arr, left, p_idx - 1)
        quick_sort(arr, p_idx + 1, right)


ex1 = [2, 1, 4, 5, 7, 1, 3, 9, 9, 2]
ex2 = [9, 5, 6, 3, 2, 8, 1, 7, 10, 4]
ex3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex4 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

for ts in (ex1, ex2, ex3, ex4):
    print "Before: %s" % ts

    with timer():
        quick_sort(ts, 0, len(ts) - 1)

    print "After: %s\n" % ts
