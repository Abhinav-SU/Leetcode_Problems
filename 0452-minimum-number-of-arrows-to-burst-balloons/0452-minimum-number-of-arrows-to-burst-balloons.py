class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda x:x[0])
        curr_x, curr_xe = 0,float('inf')
        count = 1
        for x_start,x_end in points:
            if curr_xe >= x_start:
                curr_x = max(curr_x,x_start) #1 2 10 
                curr_xe = min(curr_xe,x_end) #6 6 12
			 
            else:
                curr_x = x_start 	# 7
                curr_xe= x_end		# 12
                count += 1			# 3

        return count