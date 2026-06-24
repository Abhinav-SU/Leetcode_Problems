class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False] * n
        seen[source] = True
        stack = [source]

        while stack:
            curr_node = stack.pop()
            for nxt in graph[curr_node]:
                if nxt == destination:
                    return True
                if not seen[nxt]:
                    seen[nxt]= True
                    stack.append(nxt)

        return seen[destination]
