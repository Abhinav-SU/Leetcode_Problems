class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if not s:
            return 0
        newStr = s[:k]
        vowel = {"a", "e", "i", "o", "u"}
        count =0
        for i in range(len(newStr)):
            if newStr[i] in vowel:
                count +=1
        if len(s) <= k:
            return count
        best = count
        for indx in range(k,len(s)):
            if s[indx-k] in vowel:
                count -=1
            if s[indx] in vowel:
                count+=1
            best = max(best,count)
        return best