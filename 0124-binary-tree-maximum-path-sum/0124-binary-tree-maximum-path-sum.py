# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self,root):
        if not root:
            return 0
        maxSoFar = float('-inf')

        def maxSum(root):
            nonlocal maxSoFar

            if not root:
                return 0
            
            lh = max(maxSum(root.left),0)
            rh = max(maxSum(root.right),0)
            maxSoFar =  max(maxSoFar,(lh+rh+root.val))
            return root.val + max(lh,rh)
        maxSum(root)
        return maxSoFar
            
        