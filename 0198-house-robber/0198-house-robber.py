class Solution:
    def rob(self, nums: List[int]) -> int:

        ln = len(nums)
        if ln == 0:
            return 0
        if ln == 1:
            return nums[0]
        
        dp = [-1] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            take = nums[i] + dp[i - 2]
            not_take = 0 + dp[i - 1]
            dp[i] = max(take, not_take)
        return dp[len(nums) - 1]
