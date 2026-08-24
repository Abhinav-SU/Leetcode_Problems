# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self,root):
        if not root:
            return 0
        maxD = 0    
        def height(node):
            nonlocal maxD
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            h = 1 + max(lh,rh)
            maxD = max(maxD,lh+rh)
            return h
        height(root)
        return maxD
        