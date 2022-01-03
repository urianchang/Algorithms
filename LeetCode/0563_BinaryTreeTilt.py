# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        tilts = []
        def getTilt(node: TreeNode) -> int:
            if node == None:
                return 0

            tilt_left = getTilt(node.left)
            tilt_right = getTilt(node.right)
            tilts.append(abs(tilt_left - tilt_right))

            return node.val + tilt_left + tilt_right

        getTilt(root)
        return sum(tilts)


runner = Solution()

example_1 = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
assert runner.findTilt(example_1) == 1

example_2 = TreeNode(1)
assert runner.findTilt(example_2) == 0

example_3 = TreeNode(1, left=TreeNode(2))
assert runner.findTilt(example_3) == 2

example_4 = TreeNode(1, right=TreeNode(3))
assert runner.findTilt(example_4) == 3

example_5 = TreeNode(1, left=TreeNode(2), right=TreeNode(3, left=TreeNode(4), right=TreeNode(5)))
assert runner.findTilt(example_5) == 11

example_6 = TreeNode(4, left=TreeNode(2, left=TreeNode(3), right=TreeNode(5)), right=TreeNode(9, left=TreeNode(7)))
assert runner.findTilt(example_6) == 15
