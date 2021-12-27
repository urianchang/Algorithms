# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Results:
            1. Runtime: 80 ms
               Memory Usage: 13.9 MB

        """
        if x < 0:
            return False

        if x < 10:
            return True

        if x % 10 == 0:
            return False

        runner = 1
        while x / runner >= 10:
            runner *= 10

        while runner > 1:
            left, x = divmod(x, runner)
            x, right = divmod(x, 10)

            if left != right:
                return False

            runner //= 100

        return True


sol = Solution()
assert sol.isPalindrome(121) is True
assert sol.isPalindrome(-121) is False
assert sol.isPalindrome(10) is False
