"""
Compare two linked lists

URL: https://www.hackerrank.com/challenges/compare-two-linked-lists/problem
"""

"""
 Compare two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    r1 = headA
    r2 = headB
    while (r1 != None) and (r2 != None):
        if r1.data != r2.data:
            return 0
        r1 = r1.next
        r2 = r2.next
    return int(getattr(r1, 'data', None) == getattr(r2, 'data', None))
