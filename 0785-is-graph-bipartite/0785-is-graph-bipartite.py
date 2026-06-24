class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        for i in range(n):
            if color[i] != -1:
                continue
            color[i] = 0
            q = deque([i])
            while q:
                node = q.popleft()
                for nxt in graph[node]:
                    if color[nxt] == -1:
                        color[nxt] = 1- color[node]
                        q.append(nxt)
                    elif color[node] == color[nxt]:
                        return False
        return True