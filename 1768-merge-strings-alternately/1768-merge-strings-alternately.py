class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m=len(word1),len(word2)
        
        if n==0:
            return word1
        if m==0:
            return word2
        
        i,j=0,0
        res=""

        while i<n and j<m:
            res=res+word1[i]+word2[j]
            i+=1
            j+=1

        if i<n:
            res=res+word1[i:]

        if j<m:
            res=res+word2[j:]

        return res