# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        prev = float('-inf')
        node = root
        while node:
            if not node.left:
                if prev>=node.val:
                    return False
                prev = node.val
                node = node.right
            else:
                temp = node.left
                while temp.right and temp.right is not node:
                    temp = temp.right
                if temp.right is node:
                    temp.right = None
                    if prev >= node.val:
                        return False
                    prev = node.val
                    node = node.right
                else:
                    temp.right = node
                    node = node.left
        
        return True
    
        