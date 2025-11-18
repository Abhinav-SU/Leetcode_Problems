from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m,n = len(heights),len(heights[0])
        canReach =[[0] * n for _ in range(m)]
        atlanticQueue = deque()
        pacificQueue = deque()
        DIRECTIONS = [(0,1),(0,-1),(-1,0),(1,0)]
        PACIFIC_FLAG = 1
        ATLANTIC_FLAG = 2
        
        # 1. Initialize Queues and canReach matrix
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    pacificQueue.append((r,c))
                    canReach[r][c] |= PACIFIC_FLAG
                if r == m-1 or c == n-1:
                    atlanticQueue.append((r,c))
                    canReach[r][c] |= ATLANTIC_FLAG
        
        # --- 2. Pacific BFS ---
        q = pacificQueue
        flag = PACIFIC_FLAG
        
        while q:
            r,c = q.popleft()
            currHeight = heights[r][c]
            
            for dr,dc in DIRECTIONS:
                nr,nc = r+dr,c+dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] >= currHeight:
                        if not (canReach[nr][nc] & flag):
                            canReach[nr][nc] |= flag
                            q.append((nr,nc))

        # --- 3. Atlantic BFS ---
        q = atlanticQueue
        flag = ATLANTIC_FLAG
        
        while q:
            r,c = q.popleft()
            currHeight = heights[r][c]
            
            for dr,dc in DIRECTIONS:
                nr,nc = r+dr,c+dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    if heights[nr][nc] >= currHeight:
                        if not (canReach[nr][nc] & flag):
                            canReach[nr][nc] |= flag
                            q.append((nr,nc))
                            
        # 4. Collect Final Results
        result = []
        for r in range(m):
            for c in range(n):
                if canReach[r][c] == (PACIFIC_FLAG|ATLANTIC_FLAG):
                    result.append([r,c])
                        
        return result