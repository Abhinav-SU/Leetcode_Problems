class Solution:
    def isAnagram(self,s:str,t:str)->bool:
        m = len(s)
        n = len(t)
        if m!=n:
            return False
        count = defaultdict(int)
        for char in s:
            count[char] +=1
        for char in t:
            if count[char] == 0:
                return False
            count[char] -=1
            
        return True