    
class Solution:
    def topKFrequent(self,nums,k):
        
        numsDict ={}
        
        for num in nums:
            if num not in numsDict:
                numsDict[num] = 1
            else:
                numsDict[num] += 1
                
        topK = []
        for ke,v in numsDict.items():
            heapq.heappush(topK,(v,ke))
            if len(topK) > k:
                heapq.heappop(topK)
                
        result = []
        for v,ke in topK:
            result.append(ke)
            
        return result