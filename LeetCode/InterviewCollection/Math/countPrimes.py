# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/


from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        # Count the number of prime numbers less than a non-negative number, n
        """
        Results:
            1. Runtime: 732 ms
               Memory Usage: 36.9 MB
        """
        isPrime: List[bool] = [False, False] + [True for _ in range(2, n)]
        for i in range(2, n):
            if not isPrime[i]:
                # Already marked as not a prime number, skip!
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False

        return sum(isPrime)


s = Solution()
assert s.countPrimes(10) == 4
