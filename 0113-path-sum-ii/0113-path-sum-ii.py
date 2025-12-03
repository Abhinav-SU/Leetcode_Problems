# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def pathSum(self,root,targetSum):
		res = []
		def dfs(node,path,currSum):
			if not node:
				return
			currSum += node.val
			path.append(node.val)
			
			if not node.left and not node.right and currSum == targetSum:
				res.append(list(path))
				
			dfs(node.left,path,currSum)
			dfs(node.right,path,currSum)
			path.pop()
			
		dfs(root,[],0)
		return res
        