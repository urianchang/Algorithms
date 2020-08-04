# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        for num in nums1:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        res = []
        for num in nums2:
            if counts.get(num, 0) > 0:
                res.append(num)
                counts[num] -= 1

        return sorted(res)


assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
assert Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
