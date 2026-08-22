from collections import defaultdict               
class Solution:
    def minWindow(self,s:str,t:str)->str:
        n,m = len(s),len(t)
        if m > n:
            return ''
        frqMap = defaultdict(int)
        for char in t:
            frqMap[char] +=1
        left =0
        bestLeft = 0
        bestLen = float('inf')
        satisfied = 0
        for right in range(n):
            rightChar = s[right]
            if rightChar in frqMap:
                frqMap[rightChar] -=1
                if frqMap[rightChar] == 0:
                    satisfied +=1
            while satisfied == len(frqMap):
                leftChar = s[left]
                if leftChar in frqMap:
                    if frqMap[leftChar] == 0:
                        satisfied -=1
                    frqMap[leftChar] +=1
                curLen = right- left +1
                if curLen < bestLen:
                    bestLen = curLen
                    bestLeft = left
                left +=1
        return '' if bestLen == float('inf') else s[bestLeft:bestLeft+bestLen] 