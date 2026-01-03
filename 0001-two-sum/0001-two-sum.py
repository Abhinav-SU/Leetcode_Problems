class Solution:
	def twoSum(self,nums,target):
		
		prevMap ={}
		
		for idx,num in enumerate(nums):
			complement = target - num
			if complement in prevMap:
				return [prevMap[complement],idx]
			
			prevMap[num] = idx