
class Solution:
    def minimumEffortPath(self,heights):
        
        
        rows = len(heights)
        cols = len(heights[0])
        target =(rows-1,cols-1)


        low = 0
        high = 1000000
        min_effort = high
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
         
        def bfs(effort):
            
            q = deque([(0,0)])
            visited = set([(0,0)])
            
            while q:
                r,c = q.popleft()
                
                if (r,c) == target:
                    return True
                    
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        step_effort = abs(heights[nr][nc]-heights[r][c])
                        if step_effort <= effort and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            q.append((nr,nc))
                            
            return False
                    
        
        while low <= high:
            mid = low + (high-low)//2
            if bfs(mid):
                min_effort =mid
                high = mid - 1
            else:
                low = mid + 1
        return min_effort 