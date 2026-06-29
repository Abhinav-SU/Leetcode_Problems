# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False


        def pathSum(node,target):
            if node is None :
                return False
            
            if node.val == target and node.left is None and node.right is None:
                return True

            ra = pathSum(node.right,target-node.val)
            la = pathSum(node.left,target-node.val)
            return ra or la

        return pathSum(root,targetSum)
