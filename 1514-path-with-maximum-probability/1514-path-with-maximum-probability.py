import heapq
class Solution:
    def maxProbability(self,n,edges,succProb,start_node,end_node):
        
        #Convert edges to make a graph
        graph = [[] for i in range(n)]
        
        for (u,v),w in zip(edges,succProb):
            graph[u].append((v,w))
            graph[v].append((u,w))
            
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        
        pq = [(-1.0,start_node)]
        
        while pq:
            
           curr_prob,node =heapq.heappop(pq)
           curr_prob = -curr_prob
           
           if curr_prob < max_prob[node]:
               continue
           
           if node == end_node:
               return curr_prob
               
           for v, edge_prob in graph[node]:
               newEdge_prob = curr_prob * edge_prob
               
               if newEdge_prob > max_prob[v]:
                   max_prob[v] = newEdge_prob
                   heapq.heappush(pq,(-newEdge_prob,v))
        
        return max_prob[end_node]