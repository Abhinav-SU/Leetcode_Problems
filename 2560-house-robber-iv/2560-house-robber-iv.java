class Solution {
    public int minCapability(int[] nums, int k) {
        int minCap = 1;
        int maxCap=nums[0];
        for(int i=0;i<nums.length;i++){
            maxCap = Math.max(maxCap,nums[i]);
        }
        int len = nums.length;
        
        
        while(minCap < maxCap ){
            int midCap = ( maxCap + minCap )/2 ;
            int total_possible = 0;

            for(int i=0;i<len;++i){
                if(nums[i]<=midCap){
                    total_possible++;
                    i++;
                }       
            }

            if(total_possible>=k)
                maxCap =midCap;
            else 
                minCap =midCap+1;
        }
        
        return minCap;
    }
}