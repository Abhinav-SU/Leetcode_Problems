class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int max = nums[0];
        int min = nums[0];
        int curr_max = 0;
        int curr_min = 0;
        int total_sum = 0;
        
        for(int i =0;i< nums.length;i++){
            curr_max = Math.max(curr_max,0)+nums[i];
            max = Math.max(curr_max,max);

            curr_min =Math.min(curr_min,0)+nums[i];
            min = Math.min(curr_min,min);

            total_sum+=nums[i];
        }
        if(total_sum == min)
            return max;
        return Math.max(max,total_sum - min);
    }
}