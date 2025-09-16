class Solution {
    public int fib(int n) {
        if(n<=1)
            return n;
        
        int prev1 = 1;
        int prev2 = 0;
        int fibo= 0;
        for(int i=2; i<=n; i++){
            fibo = prev1 + prev2;
            prev2 = prev1;
            prev1 = fibo;
        }
        return fibo;
    }
}