class Solution:
	
	def permute(seld,nums):
		
		result =[]
		
		def backtrack(path):
			
			if len(nums)==len(path):
				result.append(path[:])
				return 
				
			for num in nums:
				if num in path:
					continue
					
				path.append(num)
				backtrack(path)
				path.pop()
				
		backtrack([])
		return result