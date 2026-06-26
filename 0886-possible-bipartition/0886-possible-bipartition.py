class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * n
        graph = defaultdict(list)
        
        for u,v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)

        # 0-> 1, 3 # 0
        # 1-> 0, 4 # 1
        # 2-> 0   # 1
        # 3-> 1   # 0

        for i in range(n):
            if color[i] != -1:
                continue
            color[i] = 0
            q = deque([i])
            while q:
                curr = q.popleft()
                for nxt in graph[curr]:
                    if color[nxt] == -1:
                        color[nxt] = 1 - color[curr]
                        q.append(nxt)
                    elif color[curr] == color[nxt]:
                        return False
        return True

            
                