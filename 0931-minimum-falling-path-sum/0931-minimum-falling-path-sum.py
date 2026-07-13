class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        
        def f(i,j):
            if i < 0 or i>=n:
                return float('inf')
            if j < 0 or j>=n:
                return float('inf')
            if i==0:
                return  matrix[i][j]
            if dp[i][j] != float('inf'):
                return dp[i][j]
            up = f(i-1,j)
            ldg = f(i-1,j-1)
            rdg = f(i-1,j+1)
            
            dp[i][j] = matrix[i][j] + min(up,min(ldg,rdg))
            return dp[i][j]
            
        mini = float('inf')
        
        for i in range(n):
            mini = min(mini,f(n-1,i))
            
        return mini