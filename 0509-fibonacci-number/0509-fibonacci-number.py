class Solution:
    def fib(self, n: int) -> int:
        ans = [0]*(n+1)
        
        if n < 2:
            return n
        prev =1
        prev2 = 0

        for i in range(2,n+1):
            temp = prev + prev2
            prev2 = prev
            prev = temp
        return prev
        
