# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        Results:
            1. Runtime: 208 ms
               Memory Usage: 18 MB
        """
        size = len(s)
        if size < 2:
            pass
        for i in range(size//2):
            comp = size - 1 - i
            temp = s[i]
            s[i] = s[comp]
            s[comp] = temp


test1 = ["H", "e", "l", "l", "o", "1"]
Solution().reverseString(test1)
assert test1 == ["1", "o", "l", "l", "e", "H"]
