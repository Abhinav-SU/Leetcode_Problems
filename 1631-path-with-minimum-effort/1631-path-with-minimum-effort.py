class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        dire = [(0,1),(0,-1),(1,0),(-1,0)]

        low = 0
        high = 1000000
        minEffort = high
        target =(rows -1, cols -1)


        def bfs(effort):

            q = deque([(0,0)])
            visited =set([(0,0)])

            while q:
                r,c = q.popleft()
                if (r,c) == target:
                    return True
                for dr,dc in dire:
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        minEffort = abs(heights[r][c] - heights[nr][nc])
                        if minEffort <= effort and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
            return False




        while low <=high:
            mid = (low+high)//2
            if bfs(mid):
                minEffort = mid
                high = mid -1
            else:
                low = mid + 1
        return minEffort
