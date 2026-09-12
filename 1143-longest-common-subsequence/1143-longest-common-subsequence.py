class Solution:
    def longestCommonSubsequence(self,text1,text2):
        if not text1 and not text2:
            return 0
        text1Length = len(text1)
        text2Length = len(text2)
        dp = [[-1]*text2Length for _ in range(text1Length)]
        def isCommon(indx1,indx2):
            if indx1 < 0 or indx2 < 0:
                return 0
            if dp[indx1][indx2] != -1:
                return dp[indx1][indx2]
            if (text1[indx1]==text2[indx2]):
                dp[indx1][indx2] = 1+ isCommon(indx1-1,indx2-1)
                return dp[indx1][indx2]
            dp[indx1][indx2] =  max(isCommon(indx1-1,indx2),isCommon(indx1,indx2-1))
            return dp[indx1][indx2]
        ans = isCommon(text1Length-1,text2Length-1)
        return ans