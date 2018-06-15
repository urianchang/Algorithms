# Sorting Algorithms

## Bubble sort
Simplest sorting algorithm that works by repeatedly sorting adjacent elements if
they are in the wrong order.s

__Time Complexity:__ O(n * n) [Worst case: reverse order], O(n) [Best case: already sorted]
__Auxiliary Space:__ O(1)


## Insertion sort
Like sorting cards in your hand.

__Time Complexity:__ O(n * n)
__Space Complexity:__ O(1)
__Boundary Cases:__ Maximum time to sort if elements are sorted in reverse order.
Takes minimum time (O(n)) if elements are already sorted.
__Uses:__ Used when number of elements is small. Can also be useful when input
array is almost sorted.


## Selection sort
Repeatedly find minimum element from unsorted part and putting it at the beginning.
Maintains two subarrays in a given array: sorted and unsorted.

__Time Complexity:__ O(n * n)
__Space Complexity:__ O(1)
__Uses:__ It never makes more than O(n) swaps and can be useful when memory write
is a costly operation.


## Merge sort
Divide and Conquer algorithm: divides input array in two halves, calls itself on
the two halves and then merges the two sorted halves.

__Time Complexity:__ O(n Log n)
__Space Complexity:__ O(n)
__Uses:__ Useful for sorting linked lists in O(n Log n), external sorting (handling
  large amounts of data), and inversion count (how far/close the array is from  
  being sorted).


## Quick sort
Divide and Conquer algorithm: pick an element as pivot and partitions array
around the picked pivot. All this should be done in linear time and __in place__.

Many different versions:
  1. Always pick first element as pivot
  2. Always pick last element as pivot
  3. Pick random element as pivot
  4. Pick median as pivot

Time taken by Quick sort depends on the input array and partition strategy:
  - Worst case: Partition process always picks greatest or smallest element
  as pivot O(n*n)
  - Best case: Partition process always picks the middle element as pivot O(n Log n)
  - Average case: Partition process puts O(n/9) elements in one set and O (9n/10)
  elements in other set O(n Log n)

Quick sort is faster in practice because the inner loop can be efficiently implemented
in different ways by changing the choice of pivot; however, merge sort is generally
considered better when data is huge and stored in external storage.


## Counting sort
Based on keys between a specific range. Works by counting the number of objects
having distinct key values (like hashing) and then calculating the position of
each object in the output sequence.

__Time Complexity:__ O(n + k) - n is the number of elements in the array and k
is the range of input
__Auxiliary Space:__ O(n + k)
__Additional Notes:__
  - Efficient if the range of input data is not significantly greater than number
  of objects to be sorted
  - Not comparison based sorting.
  - Often used as sub-routine to another sorting algorithm (e.g. radix sort)
  - Uses partial hashing to count occurrence of data object in O(1)
  - Can be extended to work for negative inputs


## Heap sort



## Shell sort



## Comb sort
Improvement over bubble sort by using gaps of size more than 1. The gap starts
with a large value and shrinks by a factor of 1.3 in every iteration until it
reaches the value 1.

__Time Complexity:__ O(n * n) [Worst case], O(n) [Best case]
__Auxiliary Space:__ O(1)


## Bucket sort



## Radix sort
