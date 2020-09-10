# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Results:
            1. Runtime: 44 ms
               Memory Usage: 14.1 MB

        """
        if n in (1, 2, 3):
            return n
        stairs = [1, 2, 3]
        for i in range(3, n):
            stairs.append(stairs[i-1] + stairs[i-2])
        return stairs[-1]


s = Solution()
assert s.climbStairs(2) == 2
assert s.climbStairs(3) == 3
assert s.climbStairs(4) == 5
assert s.climbStairs(5) == 8
