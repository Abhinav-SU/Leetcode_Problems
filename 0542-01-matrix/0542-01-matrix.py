class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROW = len(mat)
        COL = len(mat[0])

        q = deque()
        for i in range(ROW):
            for j in range(COL):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j]=-1


        dire =[(0,1),(0,-1),(1,0),(-1,0)]


        while q:
            r,c = q.popleft()

            for dr,dc in dire:
                nr,nc = r+dr,c+dc
                if 0 <= nr < ROW  and 0 <= nc < COL and mat[nr][nc]==-1:
                    mat[nr][nc]=mat[r][c]+1
                    q.append((nr,nc))
        return mat
