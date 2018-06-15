# Sorting Algorithms

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



## Heap sort



## Quick sort
Divide and Conquer algorithm: pick an element as pivot and partitions array
around the picked pivot. All this should be done in linear time.

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

## Bubble sort



## Shell sort



## Comb sort



## Counting sort



## Bucket sort



## Radix sort
