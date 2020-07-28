# https://leetcode.com/problems/fibonacci-number/


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1 or N == 2:
            return 1
        vals = [0, 1, 1]
        for i in range(3, N+1):
            vals.append(vals[i - 1] + vals[i - 2])
        return vals[-1]


s = Solution()
assert s.fib(2) == 1
assert s.fib(3) == 2
assert s.fib(4) == 3
