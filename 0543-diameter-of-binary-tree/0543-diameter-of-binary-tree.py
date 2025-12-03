# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def longPath(node):

            nonlocal diameter
            if not node:
                return -1

            leftH = longPath(node.left)
            rightH = longPath(node.right)

            diameter = max(diameter, leftH+rightH+2)

            return 1+max(leftH,rightH)

        longPath(root)
        return diameter

