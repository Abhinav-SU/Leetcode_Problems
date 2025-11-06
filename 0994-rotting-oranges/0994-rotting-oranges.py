from collections import deque              
class Solution:
    def orangesRotting(self,grid):
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_oranges = 0
        time = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh_oranges +=1
                elif grid[r][c]==2:
                    q.append((r,c))
                    
        if fresh_oranges == 0:
            return 0
        
        while q and fresh_oranges > 0:
            
            time +=1
            size = len(q)
            
            for _ in range(size):
                r,c = q.popleft()
                
                for dr,dc in directions:
                    nr,nc = dr+r,dc+c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        fresh_oranges -= 1
                        q.append((nr,nc))
                        
        if fresh_oranges == 0:
            return time
        else:
            return -1