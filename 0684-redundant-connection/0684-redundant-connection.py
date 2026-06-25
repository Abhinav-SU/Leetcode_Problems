class DSU:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    def _find(self,x):
        if self.root[x] == x:
            return self.root[x]
        self.root[x] = self.root[self._find(self.root[x])]
        return self.root[x]
    def _union(self,x,y):
        rootX,rootY = self._find(x), self._find(y)
        if rootX == rootY:
            return False
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] +=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)
        dsu = DSU(N+1)

        for u,v in edges:
            if not dsu._union(u,v):
                return [u,v]

        return []
