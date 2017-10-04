"""
Lily's Homework:

Whenever George asks Lily to hang out, she's busy doing homework. George
wants to help her finish it faster, but he's in over his head! Can you
help George understand Lily's homework so she can hang out with him?

Consider an array of n distinct integers, A. George can swap any two
elements of the array any number of times. An array is beautiful if the
sum of a[i] and a[i-1] among 0 < i < n is minimal possible.

Given the array A, find and print the minimum number of swaps that should
be performed in order to make the array beautiful.
"""

n = int(raw_input().strip())
A = map(int, raw_input().strip().split())

def howManySwaps(arr, n):
    # Create dictionary of int-value (key) and index (value)
    d = {}
    for idx in xrange(n):
        d[arr[idx]] = idx

    # Create sorted list
    sorted_list = sorted(arr)
    swaps = 0   # Count of swaps

    # Iterate through the input list and compare to sorted list
    for i in xrange(n):
        # If value in input list doesn't equal the one in sorted list, swap
        if arr[i] != sorted_list[i]:
            swaps += 1
            og_idx = d[sorted_list[i]]
            d[arr[i]] = d[sorted_list[i]]
            arr[i], arr[og_idx] = sorted_list[i], arr[i]

    # Return total number of swaps
    return swaps

# Check swaps for ascending order...
ascending = howManySwaps(list(A), n)    # Need to create copy of list
# Check swaps for descending order...
descending = howManySwaps(list(reversed(A)), n)
# Print the minimum number of swaps
print min(ascending, descending)

"""
Sample Input:
4
2 5 3 1

Sample Output:
2
"""
