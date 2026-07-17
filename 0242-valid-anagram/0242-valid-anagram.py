class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        s = sorted(s)
        t = sorted(t)


        for i in range(m):
            if s[i] != t[i]:
                return False
        return True

        