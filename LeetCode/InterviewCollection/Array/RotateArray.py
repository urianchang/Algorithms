# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/

from typing import List


class Solution:
    def try1(self, nums: List[int], k: int) -> None:
        """
        Runtime: 100 ms | 84 ms
        Memory Usage: 15.4 MB | 15.4 MB
        """
        p = -k % len(nums)
        nums[:] = nums[p:] + nums[:p]

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while (start <= end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def try2(self, nums: List[int], k: int) -> None:
        """
        Runtime: 88 ms | 140 ms
        Memory Usage: 15.4 MB | 15.4 MB
        """
        size = len(nums)
        self.reverse(nums, 0, size - 1)
        p = k % size
        self.reverse(nums, 0, p - 1)
        self.reverse(nums, p, size - 1)


    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.try1(nums, k)
        self.try2(nums, k)
