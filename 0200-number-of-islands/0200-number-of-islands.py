
#define unionFind class
class UnionFind:
    #define init function with parameter size
    def __init__(self,size):
        #initialzie size
        self.size =size
        #initialize list of root to track the root of each grid cell initially all cells are their own islands so we assign them value  = to their index
        self.root =[i for i in range(size)]
        #initialize rank for all these islands initially assign all of them to one 
        #this rank will be used to an optimized union operation
        self.rank = [1] * size
        #keep a count of all the islands assingn the size value to count since at start count is = to the size
        self.count = size
        
    #define find function with parameter x
    def find(self,x):
        #if x is its own root that is this element is the parent
        if x == self.root[x]:
            # return it
            return x
        #We try to get the value of root[x] until we can find such root where x is root[x] and we assign it as root[x]
        self.root[x] = self.find(self.root[x])
        #we return this new root[x]
        return self.root[x]
        
    #define union function with parameter x and yield
    def union(self,x,y):
        #initialize rootX and rootY with root of x and y
        rootX = self.find(x)
        rootY = self.find(y)
        #if the rootX and rootY is not equal we will join them together
        if rootX != rootY:
            #to join we check whose rank is greater x or y
            if self.rank[rootX] > self.rank[rootY]:
                #if x rank is greater assign the root of y to point to root of x
                self.root[rootY] = rootX
                #else if y is greater assign root of x to y
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                #if both are equal then we join root of y to x and increse rank of x by 1
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
            #we decrease the count by 1 since we have joined two cell
            self.count -= 1
            
    #define count function
    def getCount(self):
        #return the remaining count 
        return self.count
        
#define the solution class
class Solution:
    #define funtion to calculate num of islands with parameter as grid
    def numIslands(self,grid):
        # calculate row and col values of this 2d matrix as m and needed
        m,n = len(grid),len(grid[0])
        # if m is 0 or n is 0 then we dont have anything to count return 0
        if m==0 or n==0:
            return 0
           
        grid_size = m*n
        #calculate the size of the grid
        initial_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    initial_count  +=1
        #make an object of union find class and pass size to it
        uf = UnionFind(grid_size)
        uf.count = initial_count
        #now for each cell in grid we iterate and if its '1' we join all its neighbour if they are 1 as well and in boundary
        directions =[(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for dr,dc in directions:
                        nr,nc = i+dr, j+dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]=='1':
                            uf.union(i*n+j,nr*n+nc)
        #return the count from object of unionfind class
        return uf.getCount()