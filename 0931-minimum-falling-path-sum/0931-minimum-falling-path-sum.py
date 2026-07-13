class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[float('inf')] * n for _ in range(n)]
        
        for j in range(n):
            dp[0][j] = matrix[0][j]
            
        for i in range(1,n):
            for j in range(n):
                
                up  = dp[i-1][j]
                ldf = dp[i-1][j-1] if j > 0 else float('inf')
                rdf = dp[i-1][j+1] if j < n-1 else float('inf')
                
                dp[i][j] = matrix[i][j] + min(up,ldf,rdf)
                
        return min(dp[-1])