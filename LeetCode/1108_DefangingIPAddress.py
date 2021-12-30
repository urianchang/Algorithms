# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # replace every period "." with "[.]"
        return address.replace(".", "[.]")


s = Solution()
assert s.defangIPaddr(address="1.1.1.1") == "1[.]1[.]1[.]1"
assert s.defangIPaddr(address="255.100.50.0") == "255[.]100[.]50[.]0"

"""Performance results:
Runtime: 24 ms, faster than 93.75% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 14.3 MB, less than 31.37% of Python3 online submissions for Defanging an IP Address.
"""
