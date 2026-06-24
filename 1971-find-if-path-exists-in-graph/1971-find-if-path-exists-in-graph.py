class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visit = [False] * n

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visit[source]= True
        stack = [(source)]

        while stack:
            curr_node = stack.pop()
            for nxt in graph[curr_node]:
                if nxt == destination:
                    return True
                if not visit[nxt]:
                    visit[nxt]=True
                    stack.append(nxt)
            


        return visit[destination]


        