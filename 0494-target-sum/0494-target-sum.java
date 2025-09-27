class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int totalSum =0;
        for(int num:nums){
            totalSum+=num;
        }
        if(totalSum + target < 0 || (totalSum + target)%2!=0 )
            return 0;
        int dp[] = new int [(totalSum + target)/2+1];
        dp[0] =  1;
        for(int num:nums){
            for(int i =(totalSum + target)/2 ; i >= num ;i-- ){
                dp[i] = dp[i] + dp[i-num];
            }
        }
        return dp[(totalSum + target)/2];
    }
}