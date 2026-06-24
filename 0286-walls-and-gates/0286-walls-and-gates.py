class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return 
        q =deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] ==0:
                    q.append((i,j))
        dire = [(0,1),(0,-1),(1,0),(-1,0)]
        dist =0
        INF = 2147483647
        while q:
            dist +=1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr <len(rooms) and 0 <= nc < len(rooms[0]) and rooms[nr][nc] ==INF:
                        rooms[nr][nc] =dist
                        q.append((nr,nc))
                
