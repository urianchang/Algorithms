# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Results:
            1. Runtime: 28 ms
               Memory Usage: 13.9 MB

        """
        if isBadVersion(1):
            return 1

        # Binary search
        min = 1
        max = n
        while min <= max:
            mid = (min + max) // 2
            if isBadVersion(mid):
                max = mid - 1
            else:
                min = mid + 1

        return min
