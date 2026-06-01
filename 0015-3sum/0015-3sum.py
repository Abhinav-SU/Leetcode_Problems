class Solution:
	def threeSum(self,nums: List[int]) -> List[List[int]]:
		if not nums:
			return []
		nums.sort()# -4,-1,-1,0,1,2
		n = len(nums)
		answer = []
		
		
		for i in range(n-2):
			if nums[i] > 0:
				break
			if i != 0 and nums[i-1] == nums[i]:
				continue
				
			j=i+1
			k=n-1
			
			while j < k:
				current_sum =nums[i] + nums[j] + nums[k]
				if current_sum==0:
					answer.append([nums[i],nums[j],nums[k]])
					while j < k and nums[j] == nums[j+1]:
						j+=1
					while j < k and nums[k] == nums[k-1]:
						k-=1
						
					j+=1
					k-=1
				elif current_sum < 0:
					j+=1
				else:
					k-=1
					
		return answer