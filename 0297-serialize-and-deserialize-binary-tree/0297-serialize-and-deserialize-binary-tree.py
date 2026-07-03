# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data =="N":
            return 
        vals = deque(data.split(","))
        root = TreeNode(int(vals.popleft()))

        queue = deque([root])

        while queue:
            node = queue.popleft()
            left_val = vals.popleft()
            if left_val !="N":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            right_val = vals.popleft()
            if right_val !="N":
                node.right = TreeNode(int(right_val))
                queue.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))