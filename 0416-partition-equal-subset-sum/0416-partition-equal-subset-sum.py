class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        numSum = sum(nums)
        if numSum%2 !=0:
            return False
        target_sum = numSum//2
        dp = [[-1] * (target_sum + 1) for _ in range(len(nums))]
        
        def f(indx:int ,target:int)->int:
            if nums[indx] == target:
                return True
            if indx == 0:
                return nums[0] == target
            if dp[indx][target] != -1:
                return dp[indx][target]
                
            not_take = f(indx-1,target)
            take = False
            
            if target >= nums[indx]:
                take = f(indx-1,target-nums[indx])
                
            dp[indx][target] = take or not_take
            
            return dp[indx][target]
        
        return f(len(nums)-1,target_sum)