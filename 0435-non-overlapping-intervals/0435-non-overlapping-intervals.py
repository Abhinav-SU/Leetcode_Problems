class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        curr_x, curr_xe = 0,float('inf')
        count = 1
        for x_start,x_end in intervals:
            if curr_xe > x_start:
                curr_x = max(curr_x,x_start) #1
                curr_xe = min(curr_xe,x_end) #2
            else:
                curr_x = x_start 	# 
                curr_xe= x_end		# 
                count += 1			# 

        return len(intervals)-count