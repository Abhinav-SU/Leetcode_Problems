# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self,root):
        
        if not root:
            return 0
  
        def height(node,depth):
            if not node:
                return depth
            lh =  height(node.left,depth +1)
            rh =  height(node.right,depth+1)
            curH = max(lh,rh)
            
            return curH
            
        return height(root,0)
        