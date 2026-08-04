class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        arrow, end = 1, points[0][1]
        for s,e in points[1:]:
            if s > end:
                arrow +=1
                end =e
        return arrow