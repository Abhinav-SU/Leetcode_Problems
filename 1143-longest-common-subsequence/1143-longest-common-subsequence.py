         
class Solution:
    def longestCommonSubsequence(self,text1,text2):
        if not text1 or not text2:
            return 0
        len1 = len(text1)
        len2 = len(text2)
        prev = [0]*(len2+1)
        
        for i in range(1,len1+1):
            cur = [0]*(len2+1)
            for j in range(1,len2+1):
                if text1[i-1] == text2[j-1]:
                    cur[j] = 1+prev[j-1]
                else:
                    cur[j] = max(prev[j],cur[j-1])
            prev = cur
        return prev[len2]