class Solution:
    def orangesRotting(self,grid):
        if not grid:
            return -1
        row, col = len(grid),len(grid[0])
        fresh_count =0
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    fresh_count +=1
                elif grid[i][j] ==2:
                    q.append((i,j))
        time =0
        while q and fresh_count > 0:
            time +=1
            for _ in range(len(q)):
                curRow, curCol = q.popleft()
                
                for dr,dc in DIRECTIONS:
                    nr,nc = curRow + dr , curCol + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -=1
                        q.append((nr,nc))
            
            
        return time if fresh_count == 0 else -1 