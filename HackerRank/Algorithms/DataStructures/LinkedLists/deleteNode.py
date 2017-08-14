"""
Delete a Node at a given position
in a linked list.
"""

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Delete(head, position):
    if position == 0:
        head = head.next
    else:
        runner = head
        for _ in range(position - 1):
            runner = runner.next
        runner.next = runner.next.next
    return head 
