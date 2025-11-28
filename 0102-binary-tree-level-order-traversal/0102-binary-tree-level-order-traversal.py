# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return[]
        res = []
        q = deque()
        q.append(root)
		
        while q:
			
            ans =[]
            qsize = len(q)

            for _ in range(qsize):
                node = q.popleft()
                if node.left is not None: q.append(node.left)
                if node.right is not None: q.append(node.right)
                ans.append(node.val)
			
            res.append(ans)
		
        return res