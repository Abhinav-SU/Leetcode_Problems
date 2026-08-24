# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDia = 0
        def height(node):
            nonlocal maxDia 
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            h = 1 + max(lh,rh)
            maxDia = max(maxDia,(lh+rh))
            return h
        height(root)
        return maxDia