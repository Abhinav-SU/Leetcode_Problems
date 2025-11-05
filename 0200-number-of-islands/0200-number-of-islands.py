class UnionFind:
    
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
        
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
        
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                
            self.count -= 1
            
    def getCount(self):
        return self.count
        
        
class Solution:
    
    def numIslands(self,grid):
        
        rows = len(grid)
        cols = len(grid[0])
        num_nodes = rows * cols
        uf = UnionFind(num_nodes)
        
        water_count = 0
        
        direction = [[0,1],[1,0]]
        
        
        for r in range(rows):
            for c in range(cols):
                index = r * cols + c
                
                
                if grid[r][c]=='0':
                    water_count += 1
                    continue
                    
                for dr, dc in direction:
                    nr,nc = r+dr , c+dc
                    
                    if 0 <= nr < rows  and 0 <= nc < cols and grid[nr][nc]=='1':
                        nindex = nr * cols + nc 
                        uf.union(index,nindex)
                    
        return uf.getCount() - water_count