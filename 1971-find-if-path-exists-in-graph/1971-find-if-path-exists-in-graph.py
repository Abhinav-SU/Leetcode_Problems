class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        stack =[(source)]
        visited.add(source)

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nxt in graph[node]:
                if nxt == destination:
                    return True
                if nxt not in visited:
                    visited.add(nxt)
                    stack.append(nxt)

        return False


