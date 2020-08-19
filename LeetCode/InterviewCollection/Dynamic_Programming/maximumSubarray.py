# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0

        if size == 1:
            return nums[0]

        for i in range(1, size):
            # If previous value is positive, the sum can be made larger.
            # "Break" if sum is negative.
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]

        return max(nums)


s = Solution()
assert s.maxSubArray([-2, -1]) == -1
assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
