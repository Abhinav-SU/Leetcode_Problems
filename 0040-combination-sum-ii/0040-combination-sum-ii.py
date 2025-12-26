
class Solution:
	def combinationSum2(self,candidates,target):
		candidates.sort()
		result=[]
		def backtracking(start, currSum, currPath):
			if currSum == target:
				result.append(currPath[:])
				return
			if currSum > target:
				return
				
			for i in range(start, len(candidates)):
				if i > start and candidates[i] == candidates[i-1]:
					continue
				currSum += candidates[i]
				currPath.append(candidates[i])
				backtracking(i+1,currSum,currPath)
				currPath.pop()
				currSum -= candidates[i]
				
		backtracking(0,0,[])
		return result