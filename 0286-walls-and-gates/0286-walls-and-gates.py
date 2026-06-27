class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        m,n = len(rooms),len(rooms[0])
        INF = 2147483647
        q = deque()
        dire = [(0,1),(0,-1),(1,0),(-1,0)]

        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    q.append((i,j))
        dist =1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc]==INF:
                        rooms[nr][nc] = dist
                        q.append((nr,nc))
            dist +=1
        return rooms

