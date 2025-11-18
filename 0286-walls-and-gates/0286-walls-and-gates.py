class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n = len(rooms),len(rooms[0])
        q = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))
                    
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        INF = 2147483647
        
        while q:
            
            r,c = q.popleft()
            currentDistance = rooms[r][c]
            
            
            for dr,dc in directions:
                nr,nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    if rooms[nr][nc]==INF:
                        rooms[nr][nc]= currentDistance+1
                        q.append((nr,nc))