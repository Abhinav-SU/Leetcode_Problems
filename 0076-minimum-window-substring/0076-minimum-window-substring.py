from collections import defaultdict
class Solution:
    def minWindow(self,s:str,t:str)->str:
        # frequency map of t 
        # satisfied counter to check validity
        # left , right boundaries
        # bestLeft and bestLen 
        m,n = len(s),len(t)
        if n > m:
            return ''
        freqMap = defaultdict(int)
        for char in t:
            freqMap[char] +=1
        satisfied = 0

        bestLen = float('inf')
        left =0 
        bestLeft = 0
        
        for right in range(m):
            c= s[right]
            if c in freqMap:
                freqMap[c] -=1
                if freqMap[c]==0:
                    satisfied +=1
                    
            while satisfied == len(freqMap):
                currLength = right - left +1
                if currLength < bestLen:
                    bestLen = currLength
                    bestLeft = left
                leftchar = s[left]
                if leftchar in freqMap:
                    if freqMap[leftchar] == 0:
                        satisfied -=1
                    freqMap[leftchar] +=1
                left +=1
        return '' if bestLen == float('inf') else s[bestLeft:bestLeft+bestLen]