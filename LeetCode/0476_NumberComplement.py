# https://leetcode.com/problems/number-complement/
class Solution:
    def findComplement(self, num: int) -> int:
        # Flip bit by bit
        i = 1
        while num >= i:
            num ^= i 
            i <<= 1
        return num

        """Original solution...
        binary = format(num, "b")
        complement = ""
        for ch in binary:
            if ch == "0":
                complement += "1"
            else:
                complement += "0"
        return int(complement, 2)
        """


s = Solution()
assert s.findComplement(5) == 2
assert s.findComplement(1) == 0
