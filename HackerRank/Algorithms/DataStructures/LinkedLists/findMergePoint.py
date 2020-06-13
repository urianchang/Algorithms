# Python 3.7
# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
def findMergeNode(head1, head2):
    # Guaranteed that the two head Nodes will be different
    # and neither will be NULL.
    a = head1
    b = head2
    while a != b:
        if a.next is None:
            a.next = head2
        else:
            a = a.next
        if b.next is None:
            b.next = head1
        else:
            b = b.next
    return b.data
