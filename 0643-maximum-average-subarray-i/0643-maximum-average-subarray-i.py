class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums:
            return 0
        totalSum = sum(nums[:k])
        totalAvg = totalSum/k
        if len(nums) <=k:
            return totalAvg
        best = totalAvg
        for right in range(k,len(nums)):
            totalSum = totalSum + nums[right] - nums[right-k]
            totalAvg = totalSum /k
            best = max(best, totalAvg)
        return best