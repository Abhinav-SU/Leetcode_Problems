from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum_overall = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))

            # Path that potentially includes left_subtree -> node -> right_subtree
            current_path_sum = node.val + left_gain + right_gain
            self.max_path_sum_overall = max(self.max_path_sum_overall, current_path_sum)

            # Path that can be extended upwards: node + max(left_subtree_path, right_subtree_path)
            return node.val + max(left_gain, right_gain)

        dfs(root)
        return self.max_path_sum_overall