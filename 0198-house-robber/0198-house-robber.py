class Solution:
	def rob(self,nums):
		self.memo = {}
		return self.rob_top_down(len(nums)-1,nums)
		
	def rob_top_down(self,i,nums):
		if i < 0: return 0
		if i == 0: return nums[0]
		
		if i in self.memo:
			return self.memo[i]
			
		res = max(nums[i]+self.rob_top_down(i-2,nums),self.rob_top_down(i-1,nums))
		
		self.memo[i] = res
		return res