class Solution:
	def numIslands(self,grid:List[List[int]])->int:
		if not grid:
			return 0
		m = len(grid)
		n = len(grid[0])
		directions = [(0,1),(0,-1),(1,0),(-1,0)]
		count = 0
		stack = []
		
		
		def dfs(start,grid):
			stack.append(start) 
			while stack:
				r,c = stack.pop()
				for dr,dc in directions:
					nr,nc = dr+r,dc+c
					while 0 <= nr  < m and 0 <= nc < n and grid[nr][nc] == '1':
						grid[nr][nc] = '0'
						stack.append((nr,nc))
						
		for i in range(m):
			for j in range(n):
				if grid[i][j] == '1':
					count+=1
					dfs((i,j),grid)
					
		return count