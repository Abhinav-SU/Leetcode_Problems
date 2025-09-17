class Solution {
    public int tribonacci(int n) {
        if(n<=1)
            return n;
        if(n==2)
            return 1;
        int prev1 =0;
        int prev2 =1;
        int prev3 =1;
        for(int i=3;i<=n;i++){
            int temp = prev3;
            prev3 = temp+prev2+prev1;
            prev1= prev2;
            prev2=temp;
        }
        return prev3;
    }
}