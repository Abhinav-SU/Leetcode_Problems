class DSU:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size
    def find(self,x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1
            self.count -=1
    def get_count(self):
        return self.count
            
class Solution:
    def findCircleNum(self,isConnected)->int:
        dsu = DSU(len(isConnected))
        row,col = len(isConnected),len(isConnected[0])
        for i in range(row):
            for j in range(col):
                if isConnected[i][j] ==1 and i!=j:
                    dsu.union(i,j)
        return dsu.get_count()
                    