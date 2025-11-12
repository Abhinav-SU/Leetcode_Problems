class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
	
        if source == destination:
            return True
        
        
        adj =[[] for _ in range(n)]
    
        for edge in edges:
            u,v = edge
            adj[u].append(v)
            adj[v].append(u)
            
        q = deque()    
        q.append(source)
        visited = set([(source)])
            
        while q:    
            node = q.popleft()
            if node == destination:
                return True
            for neighbour in adj[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    q.append(neighbour)
                     
        return False