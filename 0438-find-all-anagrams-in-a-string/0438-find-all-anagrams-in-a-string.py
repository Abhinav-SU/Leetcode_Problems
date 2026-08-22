from collections import defaultdict
class Solution:
    def findAnagrams(self,s:str,p:str)->List[int]:
        m,n = len(s),len(p)
        if n > m:
            return []
        freqMap = defaultdict(int)
        for char in p:
            freqMap[char] +=1
        satisfied = 0
        currWindow = s[:n]
        result = []
        for char in currWindow:
            if char in freqMap:
                freqMap[char] -=1
                if freqMap[char] == 0:
                    satisfied +=1
        if satisfied == len(freqMap):
            result.append(0)
            
        for right in range(n,m):
            enterChar = s[right]
            leaveChar = s[right-n]
            
            if enterChar in freqMap:
                freqMap[enterChar] -=1
                if freqMap[enterChar] == 0:
                    satisfied +=1
            
            if leaveChar in freqMap:
                if freqMap[leaveChar] == 0:
                    satisfied -=1
                freqMap[leaveChar] +=1
            
            if satisfied == len(freqMap):
                result.append(right-n+1)
                
        return result 