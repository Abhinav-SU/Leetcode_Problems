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
        rootX , rootY = self.find(x),self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = self.root[rootX]
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = self.root[rootY]
            else:
                self.root[rootY] = self.root[rootX]
                self.rank[rootX] +=1
            self.count -= 1
 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        for u,v in edges:
            dsu.union(u,v)
        return dsu.count