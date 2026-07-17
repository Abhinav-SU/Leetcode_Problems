class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False

        count = [0] * 26
        for char in s:
            count[ord(char)-ord('a')] +=1

        for char in t:
            if count[ord(char)-ord('a')] == 0:
                return False
            count[ord(char)-ord('a')] -=1


        return True

        