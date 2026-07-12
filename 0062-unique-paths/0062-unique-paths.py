class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue

                up, left = 0, 0
                if j > 0:
                    left = dp[i][j - 1]
                if i > 0:
                    up = dp[i - 1][j]
                dp[i][j] = up + left
        return dp[m - 1][n - 1]
