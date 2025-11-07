# Swim in Rising Water 

class Solution:
    def swimInWater(self,grid):
        
        
        n = len(grid)
        low = 0
        high = 2500
        min_time =high
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        
        def canReach(time):
            
            if grid[0][0] > time:
                return False
            
            q = deque([(0,0)])
            visited = set([(0,0)])
            
            while q:
                
                r,c = q.popleft()
                
                if r == n-1 and c == n-1:
                    return True
                    
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc 
                    if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
                        cell_val = grid[nr][nc]
                        if cell_val <= time:
                            visited.add((nr,nc))
                            q.append((nr,nc))
            return False
            
        while low <= high:
            mid = low + (high-low)//2
            
            if canReach(mid):
                min_time =mid
                high = mid -1
            else:
                low = mid +1
                
        return min_time
                        
            
        
        
        
        