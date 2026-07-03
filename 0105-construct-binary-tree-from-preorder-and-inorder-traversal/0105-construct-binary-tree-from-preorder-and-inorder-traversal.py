# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {val:indx for indx , val in enumerate(inorder)}
        self.preorderIndex = 0

        def arrayToTree(left,right):
            if left > right:
                return None

            root_val = preorder[self.preorderIndex]
            root = TreeNode(root_val)
            self.preorderIndex +=1

            inorderIndex = inorderMap[root_val]

            root.left = arrayToTree(left,inorderIndex-1)
            root.right = arrayToTree(inorderIndex +1 ,right)
            return root

        return arrayToTree(0,len(preorder)-1)