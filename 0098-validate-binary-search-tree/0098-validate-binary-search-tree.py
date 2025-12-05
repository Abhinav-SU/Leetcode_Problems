# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
		
class Solution:
	def isValidBST(self,root):
		
		if not root:
			return False
		return self.validate(root,float('-inf'),float('inf'))
			
	def validate(self,node,minVal,maxVal):
			
		if not node:
			return True
				
		if not (minVal < node.val < maxVal):
			return False
				
		is_left_valid = self.validate(node.left, minVal, node.val)
		is_right_valid = self.validate(node.right,node.val,maxVal)
			
		return is_left_valid and is_right_valid
			
	
        