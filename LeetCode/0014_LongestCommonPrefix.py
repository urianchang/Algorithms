"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest word to check against
        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for word in strs:
                if word[i] != ch:
                    return shortest[:i]
        return shortest 


assert Solution().longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ""
assert Solution().longestCommonPrefix(["a"]) == "a"
