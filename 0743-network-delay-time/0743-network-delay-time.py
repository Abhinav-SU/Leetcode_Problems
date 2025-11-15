class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1,n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        INF  = float('inf')    
        dist ={i : INF for i in range(1,n+1)}
        dist[k] = 0
        
        pq =[(0,k)]
        
        while pq:
            
            current_time,u=heapq.heappop(pq)
            
            if current_time > dist[u]:
                continue
                
            for v,w in graph[u]:
                new_time = current_time + w
                
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(pq,(new_time,v))
                    
        max_delay = max(dist.values())
        
        return max_delay if max_delay != INF else -1
                