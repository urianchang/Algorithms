"""
Day 24: More Linked Lists

A Node object has an integer data field, data, and a Node
instance pointer, 'next', pointing to another node.

A 'removeDuplicates' function takes a pointer to the head Node
of a linked list as a parameter. Complete the function so that
it deletes any duplicate nodes from the list and returns the
head of the updated list.

NOTE: 'head' might be null.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self,head,data):
        p = Node(data)
        if head==None:
            head=p
        elif head.next==None:
            head.next=p
        else:
            start=head
            while(start.next!=None):
                 start=start.next
            start.next=p
        return head
    def display(self, head):
        current = head
        while current:
            print current.data,
            current = current.next
    def removeDuplicates(self, head):
        l = [head.data]
        n = head
        while n.next:
            if n.next.data in l:
                n.next = n.next.next
            else:
                l.append(n.next.data)
                n = n.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);
