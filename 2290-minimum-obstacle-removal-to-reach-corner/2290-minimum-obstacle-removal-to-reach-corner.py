#define class 
class Solution:
    #define function with graph as grid
    def minimumObstacles(self,grid):
        #initialize length of rows and cols in grid
        m,n = len(grid),len(grid[0])
        #declare queue set to track the coordinates in graph we are trying to check and also its cost to reach
        q = deque([(0,0,0)])
        #initialize a cost matrix to keep track of min cost to that cell initially all inifinity except start which will be initialize to 0
        INF = float('inf')
        dist = [[INF] * n  for _ in range(m) ]
        dist[0][0] = 0
        #initialize the directions list to traverse the neighbours
        directions =[(0,1),(1,0),(0,-1),(-1,0)]
        #traverse the grid while there is a node to traverse and we have not reached our tgarget
        while q:
            #pop out the cost to reach and x,y coordinates
            r,c,cost = q.popleft()
            #check if this cost is greater than x,y matrix cost
            if cost > dist[r][c]:
                # if yes skip
                continue
            
            #traverse its neighbour
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                #check if neighbour is a valid cell
                if 0 <= nr  < m and 0 <= nc < n:
                    #find out new edge cost
                    edge_cost = grid[nr][nc]
                    new_cost = cost + edge_cost
                    
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
                        
                        if edge_cost == 0:
                            q.appendleft((nr,nc,new_cost))
                        else:
                            q.append((nr,nc,new_cost))
#check if the coordinate can be relaxed
#update with new cost
#add to the queue based on if its a obstacle or not if its not a obstacle it can be immediately consumed in that case append to left else append to right

        final_cost = dist[m-1][n-1]
        # return final cost for the cell m-1 n-1 if its still inf return -1
        return final_cost if final_cost != INF else -1