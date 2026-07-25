class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        curr_res = []
        curr = ""

        def dfs(root, curr):
            if not root:
                return
            if not root.left and not root.right:
                return curr_res.append(curr + str(root.val))
            dfs(root.left, curr + str(root.val) + "->")
            dfs(root.right, curr + str(root.val) + "->")

        dfs(root, "")

        return curr_res
