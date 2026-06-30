# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([(root,True)])

        ans = []

        while q:
            res =[]
            current_flip = True
            for _ in range(len(q)):
                node,flip_bit = q.popleft()
                current_flip = flip_bit
                res.append(node.val)
                if node.left is not None:
                    q.append((node.left, not flip_bit))
                if node.right is not None:
                    q.append((node.right, not flip_bit))
            if not current_flip:
                res.reverse()
            ans.append(res)
        return ans



