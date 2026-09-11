class Solution:
    def climbStairs(self,n):
        dp = [-1]*(n+1)
        
        def climb(indx):
            nonlocal dp
            if indx <= 2:
                dp[indx]= indx
            if dp[indx] != -1:
                return dp[indx]
            dp[indx] = climb(indx-1)+climb(indx-2)
            return dp[indx]
        climb(n)
        return dp[n]