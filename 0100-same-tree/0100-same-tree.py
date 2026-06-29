# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None or p is not None and q is None:
            return False

        stack = [(p,q)]

        while stack:
            nodeP, nodeQ = stack.pop()
            if nodeP is None and nodeQ is None:
                continue
            if nodeP is None and nodeQ is not None or nodeP is not None and nodeQ is None:
                return False
            if nodeP.val != nodeQ.val:
                return False
            stack.append((nodeP.right,nodeQ.right))
            stack.append((nodeP.left,nodeQ.left))
        return True 
