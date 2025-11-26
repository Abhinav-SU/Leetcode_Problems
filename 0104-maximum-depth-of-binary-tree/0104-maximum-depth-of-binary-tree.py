# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth =0

        if root is None:
            return 0

        q = deque([root])

        while q:

            depth +=1

            lvl_size = len(q)

            for _ in range(lvl_size):

                curr = q.popleft()

                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)

        return depth
            