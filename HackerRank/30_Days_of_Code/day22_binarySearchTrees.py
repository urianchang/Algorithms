"""
Day 22: Binary Search Trees

The height of a binary search tree is the number
of edges between the tree's root and its furthest
leaf. You are given a pointer, root, pointing to the
root of a binary search tree. Complete the getHeight()
function so that it returns the height of the binary
search tree.
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        #Write your code here
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.right), self.getHeight(root.left))

}

T=int(raw_input())
myTree=Solution()
root=None
for i in range(T):
    data=int(raw_input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print height
