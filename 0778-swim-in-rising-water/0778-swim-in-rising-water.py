class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        dire =[(0,1),(0,-1),(1,0),(-1,0)]

        low = 0
        high = 2500
        time = high

        def canReach(time):

            if grid[0][0] > time:
                return False
            q = deque([(0,0)])
            visited = set([(0,0)])

            while q:
                r,c = q.popleft()
                if (r,c) == (rows-1,cols-1):
                    return True
                for dr,dc in dire:
                    nr,nc =r+dr,c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                        cell_val = grid[nr][nc]
                        if cell_val <= time:
                            q.append((nr,nc))
                            visited.add((nr,nc))
            return False

        


        while low <= high:
            mid = (low+high)//2
            if canReach(mid):
                time = mid
                high = mid - 1
            else:
                low = mid + 1

        return time

