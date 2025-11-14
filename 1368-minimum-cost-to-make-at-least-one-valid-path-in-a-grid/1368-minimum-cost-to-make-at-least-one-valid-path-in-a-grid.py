
#define class
class Solution:
    #define function that takes grid as input and return a min cost for a valid path
    def minCost(self,grid):
        #initialise the rows and cols for the grid
        m,n = len(grid), len(grid[0])
        #declare and initialize and dist matrix for grid that stores the min cost to get to that coordinate initially all is infinity except for start which cost 0
        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]
        dist[0][0] = 0
        
        
        #declare a queue and add to the queue the starting coordinate and its cost that is 0
        q = deque()
        q.append((0,0,0))
        
        #initialize directions info
        directions = {
                      1:(0,1),
                      2:(0,-1),
                      3:(1,0),
                      4:(-1,0)
                        }
        #define a function get_next_cell that gives us the next cell to visit based on the value of the current cell , it returns the cost associated with this travel 0 if its is travelling in the direction specified by grid cell and 1 if not
        
        def get_neighbour_info(r,c,sign_value):
            
            dr,dc = directions[sign_value]
            nr,nc = r+dr,c+dc
            
            edge_cost = 0 if grid[r][c] == sign_value else 1
            
            return nr,nc,edge_cost
         
        #Implementation of breadth first here
        
        while q:
        
            # popout the coordinate and cost to get to that coordinate 
            r,c,cost = q.popleft()
            
            # check if that cost is grater than the cost in dist matrix if so we can skip this iteration
            if cost > dist[r][c]:
                continue
            
            if r == m-1 and c == n-1:
                return cost
            
            #calculate the new edge cost of the neighbors and get them  through the function defined above
            
            for sign_value in range(1,5):
                nr,nc,edge_cost = get_neighbour_info(r,c,sign_value)
                
                #check boundary 
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost + edge_cost
                    
                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost
            
                    #relax the edges based on the new edge cost 
                        if edge_cost == 0:
                            q.appendleft((nr,nc,new_cost))
                    #if the edge cost was 0 append it to the left to consume it early
                        else:
                            q.append((nr,nc,new_cost))
                    #if 1 then append to the right 
            
        #check if the cost in grid rows-1 and cols-1 is not infinity then return otherwise return -1
        return -1