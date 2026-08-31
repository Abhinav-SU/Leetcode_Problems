class Solution:
    def numIslands(self,grid:List[List[str]])-> int:
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def bfs(row,col):
            q =  deque()
            q.append((row,col))
            grid[row][col] ="0"
            while q:
                r,c = q.popleft()
                
                for dr,dc in DIRECTIONS:
                    nr,nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <=nc <n and grid[nr][nc] == '1':
                        grid[nr][nc]="0"
                        q.append((nr,nc))
        island_count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    island_count +=1
                    bfs(i,j)
        return island_count