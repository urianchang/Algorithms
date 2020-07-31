# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Optimized with XOR operation
        for i in range(1, len(nums)):
            nums[0] = nums[0] ^ nums[i]
        return nums[0]

        # Original submission...
        # seen = {}
        # for num in nums:
        #     if num not in seen:
        #         seen[num] = 1
        #     else:
        #         seen[num] += 1
        # for k, v in seen.items():
        #     if v == 1:
        #         return k
