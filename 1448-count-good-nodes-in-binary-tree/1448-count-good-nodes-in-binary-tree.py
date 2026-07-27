# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        maxSoFar = root.val

        def dfs(root, maxSoFar):
            nonlocal count
            if not root:
                return
            if root.val >= maxSoFar:
                count += 1

            maxSoFar = max(root.val, maxSoFar)
            if root.left:
                dfs(root.left, maxSoFar)
            if root.right:
                dfs(root.right, maxSoFar)

        dfs(root, maxSoFar)
        return count
