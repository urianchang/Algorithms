"""
Get Node Value

URL: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
"""

"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    if not head:
        return head
    count = 0
    node_map = {}
    runner = head
    while runner:
        count += 1
        node_map[count] = runner.data
        runner = runner.next
    return node_map[count-position]
