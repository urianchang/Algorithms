# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Given an integer, write a function to determine if it is a
        # power of three.
        """
        Results:
            1. Runtime: 112 ms
               Memory Usage: 13.9 MB

        """
        if n < 1:
            return False

        while n % 3 == 0 and n != 0:
            n /= 3

        return n == 1


s = Solution()
assert s.isPowerOfThree(27) is True
assert s.isPowerOfThree(0) is False
assert s.isPowerOfThree(45) is False
