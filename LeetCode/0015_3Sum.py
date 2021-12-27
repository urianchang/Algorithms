# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def brute(self, nums: List[int]) -> List[List[int]]:
        # Brute force ==> timed out on some problems
        res = {}
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    arr = sorted([nums[i], nums[j], nums[k]])
                    if sum(arr) == 0:
                        res[str(arr)] = arr
        return res.values()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """Given an array of integers, find all unique triplets in the array
        which gives the sum of zero.

        Note: The solution set must not contain duplicate triplets.

        Results:
            1. Runtime: 1140 ms
               Memory Usage: 17.2 MB

        """
        res = []
        length = len(nums)
        nums.sort()
        for i in range(length - 2):
            if nums[i] > 0:
                # All numbers in front of this one is positive,
                # so it's impossible to get 0
                break

            if i > 0 and nums[i] == nums[i - 1]:
                # Skip processing duplicates
                continue

            mid = i + 1
            right = length - 1

            while mid < right:
                total = nums[i] + nums[mid] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    mid += 1
                else:  # total = 0
                    res.append([nums[i], nums[mid], nums[right]])

                    # skip through duplicates
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1

                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1

                    mid += 1
                    right -= 1

        return res
