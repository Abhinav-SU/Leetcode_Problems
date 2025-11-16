from typing import List

## \U0001f5fa️ UnionFind Class for Area Tracking
class UnionFind:
    """
    Union-Find structure modified for the Max Area of Island problem.
    It tracks the size (area) of the set at its root and the global maximum area.
    """
    def __init__(self, size):
        self.size = size
        self.root = list(range(size))
        # rank is used for optimization (Union by Rank)
        self.rank = [1] * size 
        # area tracks the size of the set whose root is at index i.
        # Initialized to 1 for every cell, but only land cells will use this area.
        self.area = [1] * size 
        # Global maximum area found so far.
        self.max_area = 0

    def find(self, x):
        if x == self.root[x]:
            return x
        # Path compression
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by Rank
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                # Area update: add Y's area to X's area (X is new root)
                self.area[rootX] += self.area[rootY]
                new_root_area = self.area[rootX]
            
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                # Area update: add X's area to Y's area (Y is new root)
                self.area[rootY] += self.area[rootX]
                new_root_area = self.area[rootY]

            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
                # Area update: add Y's area to X's area (X is new root)
                self.area[rootX] += self.area[rootY]
                new_root_area = self.area[rootX]
            
            # Update global maximum area
            self.max_area = max(self.max_area, new_root_area)
            
            return True 
        return False
    
    def getMaxArea(self):
        return self.max_area


## \U0001f6a2 Solution Class Implementation
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        uf = UnionFind(R * C)
        
        # Helper function to map 2D coordinates to 1D index
        def get_id(r, c):
            return r * C + c

        # Phase 1: Initialize Area and Track Smallest Possible Max Area (1)
        # We must initialize the area array correctly for *only* land cells.
        initial_max_area = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    cell_id = get_id(r, c)
                    # The UF class already sets area[id] = 1 upon initialization,
                    # but we track the max here in case there are only single cells.
                    initial_max_area = 1
                else:
                    # Crucial: Water cells must not contribute to area calculation
                    uf.area[get_id(r, c)] = 0
        
        # Set the initial max_area based on initialization
        uf.max_area = initial_max_area

        # Phase 2: Union Operations (Connect Neighbors)
        # Iterate through the grid and union adjacent land cells.
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    current_id = get_id(r, c)
                    
                    # Connect to right neighbor
                    if c + 1 < C and grid[r][c + 1] == 1:
                        uf.union(current_id, get_id(r, c + 1))

                    # Connect to down neighbor
                    if r + 1 < R and grid[r + 1][c] == 1:
                        uf.union(current_id, get_id(r + 1, c))

        # Phase 3: Return Result
        return uf.getMaxArea()