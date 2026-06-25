class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u,v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        color = [-1] * n
        for i in range(n):
            if color[i] != -1:
                continue
            color[i]=0
            q=deque([i])
            while q:
                node = q.popleft()
                for nxt in graph[node]:
                    if color[nxt] == -1:
                        color[nxt]=1-color[node]
                        q.append(nxt)
                    elif color[nxt] == color[node]:
                        return False
        return True