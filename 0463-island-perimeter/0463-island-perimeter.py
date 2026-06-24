class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        res =0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    res +=4
                    if i > 0 and grid[i-1][j]==1:
                        res -=2
                    if j > 0 and grid[i][j-1]==1:
                        res -=2

        return res

