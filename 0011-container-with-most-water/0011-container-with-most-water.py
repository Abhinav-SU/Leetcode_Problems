
class Solution:
    def maxArea(self,height:List[int])->int:
        if not height:
            return 0
        containerLen = len(height)
        left = 0 
        right = containerLen-1
        maxA = 0
        while left < right:
            curArea = min(height[left],height[right]) * (right-left)
            maxA = max(maxA,curArea)
            if height[left] <=height[right]:
                left +=1
            else:
                right -=1
        return maxA