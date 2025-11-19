import heapq        
class Solution:
    def findKthLargest(self,nums,k):
        q =[]
        
        for num in nums:
            heappush(q,num)
            if len(q) > k:
                heappop(q)
                
        return heappop(q)