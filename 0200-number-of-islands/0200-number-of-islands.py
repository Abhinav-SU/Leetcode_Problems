        
class Solution:
    
    def numIslands(self,grid):
        
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs_sink(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == '0':
                return
            
            grid[r][c]='0'
            
            for dr,dc in directions:
                dfs_sink(r+dr,c+dc)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    island_count +=1                
                    dfs_sink(r,c)
        return island_count
