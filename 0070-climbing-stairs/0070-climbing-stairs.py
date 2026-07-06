class Solution:
    def climbStairs(self, n: int) -> int:
        a= 1
        b=2
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(1,n-1):
            res = a+b
            a =b
            b = res
        return res
