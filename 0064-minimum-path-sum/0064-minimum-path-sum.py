
class Solution:
    def minPathSum(self,grid: [List[List[int]]])->int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        def f(i,j):
            if i == 0 and j ==0:
                return dp[0][0]
            if i < 0 or j < 0:
                return float('inf')
            if dp[i][j] != float('inf'):
                return dp[i][j]
            up,left =float('inf'),float('inf')
            if i > 0:
                up = f(i-1,j)
            if j > 0:
                left = f(i,j-1)
                
            dp[i][j] = grid[i][j] + min(up,left)
            
            return dp[i][j]
            
        return f(m-1,n-1)