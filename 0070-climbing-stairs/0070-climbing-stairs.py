class Solution:
	def climbStairs(self,n):
		prev1 =1 #no of ways to reach 1st stair
		prev2 =2 #no of ways to reach 2nd stair 
		count =0
		if n==1:
			return prev1
		elif n==2:
			return prev2
		else:
			for i in range(3,n+1):
				count = prev1 + prev2
				prev1 = prev2
				prev2 = count
				
		return count