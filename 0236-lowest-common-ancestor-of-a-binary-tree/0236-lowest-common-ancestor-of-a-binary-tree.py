# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        foundP,foundQ = False,False
        
        def recurse(node):
            nonlocal foundP,foundQ
            if not node:
                return None
            
            left = recurse(node.left)
            right = recurse(node.right)
            
            if node == p:
                foundP = True
                return node
            if node == q:
                foundQ = True
                return node
            if left and right:
                return node
            return left or right
            
        result = recurse(root)
        return result if foundP and foundQ else None