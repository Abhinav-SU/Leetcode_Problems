class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum+num,num)
            maxSum = max(currSum,maxSum)
        return maxSum

