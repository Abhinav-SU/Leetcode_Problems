import heapq
class Solution:
    def maxProbability(self,n,edges,succProb,start_node,end_node):
        
        
        graph =[[] for _ in range(n)]
        
        for (u,v),w in zip(edges,succProb):
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        maxProb = [0.0] * n
        maxProb[start_node] = -1.0
            
        pq = [(-1.0,start_node)]
            
            
        while pq:
                
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob = -curr_prob
                
            if curr_prob < maxProb[curr_node]:
                continue
                
            if curr_node == end_node:
                return curr_prob
                    
            for v,edge_prob in graph[curr_node]:
                newEdgeProb = curr_prob * edge_prob
                    
                    
                if newEdgeProb > maxProb[v]:
                    maxProb[v] = newEdgeProb
                    heapq.heappush(pq,(-newEdgeProb,v))
                        
        return maxProb[end_node]