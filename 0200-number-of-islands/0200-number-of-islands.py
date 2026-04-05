class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0


        def dfs(r,c):
            # Check boundary
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] =='0':
                return
            # mark the current cell to be visited
            grid[r][c] = '0' 
            #process and traverse
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                dfs(r+dr , c+dc)
 

            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    num_islands += 1

        return num_islands