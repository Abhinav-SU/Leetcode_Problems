# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack =[(root,-math.inf,math.inf)]
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            val = node.val
            if val <= low or val >= high:
                return False
            stack.append((node.right,val,high))
            stack.append((node.left, low, val))
        return True
            
