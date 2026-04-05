class Solution:
	def maxAreaOfIsland(self,grid):
		if not grid:
			return 0
			
		n = len(grid)#12
		m = len(grid[0])#7
		result = 0
		directions = [(0,1),(1,0),(0,-1),(-1,0)]
		
		def dfs(r,c):
			if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] != 1:
				return 0
				
			grid[r][c] = 0
			area = 1
			
			for dr,dc in directions:
				area += dfs(r+dr,c+dc)
			return area	
			
		for i in range(n):
			for j in range(m):
				if grid[i][j]==1:
					result =max(result,dfs(i,j))
		return result