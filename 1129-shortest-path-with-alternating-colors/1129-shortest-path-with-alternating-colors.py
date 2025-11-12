class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)
        
        for edge in redEdges:
            u,v = edge
            red[u].append(v)
            
        for edge in blueEdges:
            u,v = edge
            blue[u].append(v)  

        answer = [ -1 for _ in range(n)]
        q = deque()
        q.append([0,0,None]) #vertex , length , color
        visit = set()
        visit.add((0,None))
        
        
        while q:
            node,length,colorEdge = q.popleft()
            
            if answer[node]==-1:
                answer[node] = length
                
            
            if colorEdge != 'RED':
                for nei in red[node]:
                    if (nei,'RED') not in visit:
                        visit.add((nei,'RED'))
                        q.append([nei,length+1,'RED'])
                        
            if colorEdge != 'BLUE':
                for nei in blue[node]:
                    if (nei,'BLUE') not in visit:
                        visit.add((nei,'BLUE'))
                        q.append([nei,length+1,'BLUE'])
                        
        return answer