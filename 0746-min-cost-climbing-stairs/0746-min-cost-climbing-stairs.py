class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # prev2 is cost to reach 2 steps back, prev1 is 1 step back
        prev2, prev1 = 0, 0
        
        # We want to reach the index 'len(cost)', which is the floor beyond the last step
        for i in range(2, len(cost) + 1):
            # Cost to reach current step 'i'
            current = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2, prev1 = prev1, current
            
        return prev1