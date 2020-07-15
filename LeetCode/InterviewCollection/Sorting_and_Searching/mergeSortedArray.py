# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Results:
            1. Runtime: 36 ms
               Memory Usage: 13.7 MB

        """
        # Place larger value at 'end' cursor
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # Any more values in nums2 that were smaller than all in nums1
        # add to head
        if n > 0:
            nums1[:n] = nums2[:n]
