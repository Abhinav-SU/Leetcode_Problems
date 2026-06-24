class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        dire =[(0,1),(0,-1),(1,0),(-1,0)]
        count = 0

        def dfs(start_r,start_c):
            stack = [(start_r,start_c)]
            grid[start_r][start_c] ='0'
            while stack:
                r,c = stack.pop()
                for dr,dc in dire:
                    nr,nc = r+dr , c+dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc]=='1':
                        grid[nr][nc] ='0'
                        stack.append((nr,nc))

        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    count +=1
                    dfs(i,j)
        return count