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


"""
Sample Input:
4
2 5 3 1

Sample Output:
2
"""
