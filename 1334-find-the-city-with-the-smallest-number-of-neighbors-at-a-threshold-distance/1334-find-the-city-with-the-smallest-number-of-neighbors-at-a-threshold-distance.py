class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')] * n for _ in range(n)]

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            distance[u][v] = wt
            distance[v][u] = wt
        
        for i in range(n):
            distance[i][i] = 0

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][via]== float('inf') or distance[via][j] ==float('inf'):
                        continue
                    distance[i][j] =min(distance[i][j], distance[i][via] + distance[via][j])
        maxCount = n
        cityNo =-1

        for i in range(n):
            cnt =0
            for j in range(n):
                
                if distance[i][j] <= distanceThreshold:
                    cnt+=1

            if cnt <= maxCount:
                maxCount = cnt
                cityNo = i
        return cityNo
