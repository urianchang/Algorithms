"""
Day 15: Linked List

A Node class is provided. A Node object has an integer data field,
data, and a Node instance pointer, 'next', pointing to another node.

A Node insert function is also declared. It has two parameters: a pointer,
'head', pointing to the first node of a linked list, and an integer data
value that must be added to the end of the list as a new Node object.

Complete the insert function in your editor so that it creates a new Node
(pass data as the Node constructor argument) and inserts it at the tail of
the linked list reference by the head parameter. Once the new node is added,
return the reference to the head node.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self, head, data):
        if head == None:
            head = Node(data)
        else:
            runner = head
            while runner.next:
                runner = runner.next
            runner.next = Node(data)
        return head

mylist = Solution()
T = int(raw_input())
head = None
for i in range(T):
    data = int(raw_input())
    head = mylist.insert(head, data)
mylist.display(head)
