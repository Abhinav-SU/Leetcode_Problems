class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        
        #initialize
        m,n = len(grid),len(grid[0])
        #iniitialize queue and visited set
        q = deque()
        visited = set()
        #initialize directions
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        #Find the start of the traversal add to queue and visited set , in q we will have the coordinates and current distance form start so initially  it will be r,c,0
        start_r,start_c = -1,-1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    start_r,start_c = i,j
                    break

        if start_r != -1 and start_c != -1:
            q.append((start_r,start_c,0))
            visited.add((start_r,start_c))
        else:
            return -1
        
        #BFS on the grid till we find shortest path
        while q:
            #pop out the r,c,distance tuple in queue
            r,c,distance = q.popleft()

            #check the grid we are visiting is our target
            if grid[r][c] == '#':
                return distance
                
                #if yes resturn the distance 
            
        #if not visit each neighbour of the current coordinate if its not an obstace
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0<= nr < m and 0 <= nc < n and grid[nr][nc]!='X':
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc,distance+1))
                    
        # add to the visited set and to the queue
        
        #return -1 if no path has been find till yet
        return -1