class Solution:
    def climbStairs(self, n: int) -> int:
        prev1,prev2 =1,2
        if n == 1:
            return prev1
        if n== 2:
            return prev2
        for i in range(3,n+1):
            stairCount = prev1 + prev2
            prev1 = prev2
            prev2 = stairCount
            
        return prev2