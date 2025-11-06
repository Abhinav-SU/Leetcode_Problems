from collections import deque
class Solution:
    def minKnightMoves(self,x,y):
        
        q = deque()
        q.append((0,0,0))
        visited = set([(0,0)])
        directions = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        
        
        while q:
            
            r,c,moves = q.popleft()
            
            if r==x and c==y:
                return moves
                
                
            for dr,dc in directions:
                nr , nc = r + dr , c + dc
                if (nr,nc) not in visited:
                    visited.add((nr,nc))
                    q.append((nr,nc,moves+1))
                    
        return -1