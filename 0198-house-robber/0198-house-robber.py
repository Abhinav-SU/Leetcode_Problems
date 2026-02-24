class Solution:
	def rob(self,nums):
		n = len(nums)
		
		prev1 = 0
		prev2 = 0

		
		for x in nums:
			curr = max(x+prev2,prev1)
			prev2 = prev1
			prev1 = curr
		
		return prev1