# Count island using bfs
from collections import deque
class Solution:
    
    def numIslands(self,grid):
        
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs(r,c):
            
            
            q = deque()
            q.append((r,c))
            grid[r][c] = '0'
            
            while q:
                nr , nc = q.popleft()
                
                for dr, dc in directions:
                    nrow, ncol = nr + dr , nc +dc
                    if 0 <= nrow < rows and 0 <= ncol < cols:
                        if grid[nrow][ncol] == '1':
                            grid[nrow][ncol] = '0'
                            q.append((nrow,ncol))
        island_count = 0    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island_count+=1
                    bfs(r,c)
        return island_count
                    
        
            
            