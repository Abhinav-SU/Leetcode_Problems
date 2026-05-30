class Solution:
	def trap(self,height:List[int])->int:
		if not height:
			return 0
		n = len(height)
		left,right = 0,n-1
		maxLeft,maxRight =height[left],height[right]
		totalTrapped =0
		
		while left < right:
			#check the bottleneck between left and right
			if height[left] <= height[right]:
				#move the left pointer as it can be processed
				left+=1
				maxLeft =  max(maxLeft,height[left])
				totalTrapped += maxLeft - height[left]
			else:
				right-=1
				maxRight = max(maxRight,height[right])
				totalTrapped += maxRight - height[right]
				
		return totalTrapped