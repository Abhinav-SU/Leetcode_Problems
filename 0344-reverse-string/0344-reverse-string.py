class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        for i in range(0,len(s)//2):
            temp = s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=temp
        """

        l,r=0,len(s)-1
        while l<r:
            temp =s[l]
            s[r]=s[l]
            s[l]=temp
            r++
            l--