class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        s="".join(ch for ch in s if ch.isalnum()).lower()
        for i in range(0,len(s)//2):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
        """
        s="".join(ch for ch in s if ch.isalnum()).lower()
        n,l,r=len(s),0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True


