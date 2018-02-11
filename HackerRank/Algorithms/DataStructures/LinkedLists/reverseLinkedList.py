"""
Reverse a linked list

URL: https://www.hackerrank.com/challenges/reverse-a-linked-list

Head could be None as well for empty list

Node is defined as:

class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    pre = None
    cur = head
    nex = None
    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex
    head = pre
    return head
