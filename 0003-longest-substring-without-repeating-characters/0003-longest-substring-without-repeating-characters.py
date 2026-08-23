class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        if not s:
            return 0
        strlen = len(s)
        charToIndxMap = defaultdict(int)
        
        left = 0
        bestLen = float('-inf')
        
        for right in range(strlen):
            if s[right] in charToIndxMap and charToIndxMap[s[right]] >= left:
                left = charToIndxMap[s[right]]+1
            charToIndxMap[s[right]] = right
            curLen = right - left +1
            bestLen = max(bestLen,curLen)
        return bestLen