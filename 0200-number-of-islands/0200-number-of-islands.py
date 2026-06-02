class Solution:
	def numIslands(self,grid: List[List[int]]) -> int:
		if not grid:
			return 0
		m,n =len(grid),len(grid[0])
		if m==0 and n==0:
			return 0
		count =0 
		directions = [(0,1),(0,-1),(1,0),(-1,0)]
		
		def dfs(start_r,start_c):
			stack =[(start_r,start_c)]
			grid[start_r][start_c]='0'
			

			while stack:
				r,c = stack.pop()
				for dr,dc in directions:
					nr,nc = r+dr,c+dc
					if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]=='1':
						stack.append((nr,nc))
						grid[nr][nc]='0'
		for i in range(m):
			for j in range(n):
				if grid[i][j]=='1':
					dfs(i,j)
					count+=1
		return count 