# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def deleteNode(self,root,key):
		
		if root is None:
			return root
		
		if key < root.val:
			root.left = self.deleteNode(root.left,key)
			return root
		elif key > root.val:
			root.right = self.deleteNode(root.right,key)
			return root
		else:
			if root.left is None:
				return root.right
			elif root.right is None:
				return root.left
			
			successor = self.findMin(root.right)
			root.val = successor.val
			root.right = self.deleteNode(root.right, successor.val)
			return root
			
	def findMin(self,node):
		current = node
		while current.left:
			current=current.left
		return current