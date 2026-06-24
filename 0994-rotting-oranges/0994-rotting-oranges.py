class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        q = deque()
        dire =[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh +=1
                if grid[i][j]==2:
                    q.append((i,j))
        time = 0
        while q and fresh > 0:
            time +=1
            for _ in range(len(q)):
                r,c =q.popleft()
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc]==1:
                        fresh -=1
                        grid[nr][nc] =2
                        q.append((nr,nc))
        
        return time if fresh==0 else -1

