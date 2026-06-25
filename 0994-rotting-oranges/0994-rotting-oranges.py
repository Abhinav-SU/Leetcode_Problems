class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        time =0
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                if grid[i][j]==1:
                    fresh +=1

        while q and fresh > 0:
            
            for _ in range(len(q)):
                r,c = q.popleft()
                
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr <m and 0 <= nc <n and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh -=1
                        q.append((nr,nc))
            time +=1
        return time if fresh==0 else -1

                    