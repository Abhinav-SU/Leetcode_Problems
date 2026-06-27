class DSU:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self,x):
        if self.root[x] == x:
            return self.root[x]
        self.root[x] = self.root[self.find(self.root[x])]
        return self.root[x]

    def union(self,x,y):
        rootX,rootY = self.find(x),self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = self.root[rootX]
                self.rank[rootX] +=1
            self.count -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu = DSU(n)

        for u in range(n):
            for v in range(n):
                if isConnected[u][v] ==1:
                    dsu.union(u,v)
        return dsu.count