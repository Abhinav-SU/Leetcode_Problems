class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                else:
                    up, left = 0, 0
                    if j > 0:
                        left = dp[i][j - 1]
                    if i > 0:
                        up = dp[i - 1][j]
                    dp[i][j] = up + left
        return dp[m - 1][n - 1]
