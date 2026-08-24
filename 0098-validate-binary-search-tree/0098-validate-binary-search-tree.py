# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self,root):
        if not root:
            return True
        prev = float('-inf')    
        def dfs(node):
            nonlocal prev
            if not node:
                return True
            if not dfs(node.left):
                return False
            if node.val <= prev:
                return False
            prev = node.val
            return dfs(node.right)
        return dfs(root)
        