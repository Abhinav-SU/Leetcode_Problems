class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))

        q = deque([0])
        visited = set()
        visited.add(0)
        change = 0


        while q:
            curr_city = q.popleft()
            for nxt,is_forw in graph[curr_city]:
                if nxt not in visited:
                    visited.add(nxt)
                    change += is_forw
                    q.append(nxt)

        return change