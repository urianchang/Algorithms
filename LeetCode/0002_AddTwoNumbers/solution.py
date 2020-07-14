# https://leetcode.com/problems/add-two-numbers/
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Results:
            1. Runtime: 84 ms
               Memory Usage: 14 MB
        """
        val = 0
        res = cur = ListNode(0)  # We skip the initial node

        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            val, rem = divmod(val, 10)
            cur.next = cur = ListNode(rem)

        return res.next
