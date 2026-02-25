class Solution:
	def minCostClimbingStairs(self,cost):
		memo = {}
		n = len(cost)


		def f(i,cost):
			
			
			if i<2:
				return 0
			
			if i in memo:
				return memo[i]
			res = min(f(i-2,cost)+cost[i-2],f(i-1,cost)+cost[i-1])

			memo[i] = res

			return res
			
		return f(n,cost)