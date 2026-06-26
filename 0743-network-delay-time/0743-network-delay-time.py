class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        dist = [float('inf')] * (n+1)
        dist[k] = 0

        pq = [(0,k)]

        while pq:

            d,node = heapq.heappop(pq)

            if d > dist[node]:
                continue
            for nxt,w in graph[node]:
                nd = d + w
                if nd < dist[nxt]:
                    dist[nxt] = nd
                    heapq.heappush(pq,(nd,nxt))
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1