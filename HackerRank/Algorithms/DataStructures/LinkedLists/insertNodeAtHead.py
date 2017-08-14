'''
Insert node at head of linked list.
Head input could be null.
Return back to head node.
'''

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if head == None:
        head = Node(data)
    else:
