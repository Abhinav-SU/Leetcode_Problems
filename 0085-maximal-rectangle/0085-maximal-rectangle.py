class Solution:
    def maxHistogram(self,heights: List[int])->int:
        stack = [] # pair of index, height
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >h:
                index,height = stack.pop()
                maxArea = max(maxArea , height * (i - index))
                start = index
            stack.append((start,h))

        for index, height in stack:
            maxArea = max(maxArea, height *(len(heights)-index))
        
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxArea = 0

        heights = [0]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            maxArea = max(maxArea , self.maxHistogram(heights))
        
        return maxArea

    
