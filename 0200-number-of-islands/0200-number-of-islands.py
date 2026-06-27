class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        dire =[(0,1),(0,-1),(1,0),(-1,0)]
        count =0

        def dfs(r,c):
            stack =[(r,c)]
            while stack:
                sr,sc = stack.pop()
                grid[sr][sc] = 0
                for dr,dc in dire:
                    nr,nc = sr+dr,sc+dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]=='1':
                        stack.append((nr,nc))
                    


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count +=1
                    dfs(i,j)
        return count 