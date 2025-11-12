class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #low is min weight in weights
        low = max(weights)        
        #high is sum of all weights if ship has that cap then can be shipped in 1day
        high = sum(weights)
        #result , to track the result
        result = high
        #binary search on ship cap
        while low <= high:
        #calculate mid
            mid = low + (high-low)//2
            currD = 1
            currW = 0
            for weight in weights:
                if currW + weight <= mid:
                    currW += weight
                else:
                    currD+=1
                    currW = weight
                    
            if currD <= days:
                high = mid -1
                result = mid
            else:
                low = mid +1
                
        return result