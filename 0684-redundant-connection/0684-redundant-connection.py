class DSU:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,x):
        if self.root[x] == x:
            return self.root[x]
        self.root[x] = self.root[self.find(self.root[x])]
        return self.root[x]

    def union(self,x,y):
        rootX,rootY = self.find(x), self.find(y)

        if rootX == rootY:
            return False
        
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges)+1)

        for u,v in edges:
            if not dsu.union(u,v):
                return [u,v]
        return []
            