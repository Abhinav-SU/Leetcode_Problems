
class Solution:
	def combinationSum(self,candidates,target):
		result=[]
		def backtracking(start, currSum, currPath):
			if currSum == target:
				result.append(currPath[:])
				return
			if currSum > target:
				return
				
			for i in range(start, len(candidates)):
				currSum += candidates[i]
				currPath.append(candidates[i])
				backtracking(i,currSum,currPath)
				currPath.pop()
				currSum -= candidates[i]
				
		backtracking(0,0,[])
		return result