
class Solution:
    def solve(self,board):
        if not board:
            return
        m,n = len(board),len(board[0])
        queue = deque()
        for row in range(m):
            for col in range(n):
                if board[row][col] =="O" and (row == 0 or row == m-1 or col ==0 or col ==n-1):
                    queue.append((row,col))
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            row,col = queue.popleft()
            board[row][col] ="#"
            for dr,dc in DIRECTIONS:
                nr,nc = row+dr, col+dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    queue.append((nr,nc))
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "#":
                    board[row][col] = "O"
        return