class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) ==1:
	        return stones[0]

        for i in range(1,len(stones)):
            stones.sort(reverse=True)
            if stones[i-1]==stones[i]:
                stones[i]=0
            elif stones[i-1]!=stones[i]:
                stones[i]= math.fabs(stones[i-1] - stones[i])
                

        return int(stones[-1])