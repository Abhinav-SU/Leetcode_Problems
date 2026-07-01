# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def build_graph(cur,parent):
            if cur and parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            if cur.left:
                build_graph(cur.left,cur)
            if cur.right:
                build_graph(cur.right,cur)

        build_graph(root,None)

        answer = []
        visited = set([target.val])
        
        queue = deque([(target.val,0)])
        while queue:
            cur,distance = queue.popleft()
            if distance == k:
                answer.append(cur)
                continue

            for nei in graph[cur]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei,distance+1))

        return answer


