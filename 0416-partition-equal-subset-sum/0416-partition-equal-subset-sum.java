class Solution {
    public boolean canPartition(int[] nums) {
        int total_sum =0;
        for(int num:nums)
            total_sum+=num;
        if(total_sum%2!=0){
            return false;
        }
        int subset_sum=total_sum/2;
        boolean dp[] = new boolean[subset_sum+1];
        dp[0] =true;
        for(int num:nums){
            for(int i=subset_sum ;i>=num;i--){
                dp[i]=dp[i]|dp[i-num];
            }
        }
        return dp[subset_sum];
    }
}