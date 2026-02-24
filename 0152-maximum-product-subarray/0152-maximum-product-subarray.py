class Solution:
	def maxProduct(self,nums):
		maxSoFar = nums[0]
		minSoFar = nums[0]
		result = nums[0]
		
		for i in range(1, len(nums)):
			curr = (nums[i], maxSoFar * nums[i], minSoFar * nums[i])
			maxSoFar = max(curr)
			minSoFar = min(curr)
			result = max(result,maxSoFar)
			
		return result