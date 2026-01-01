class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x:x[1]-x[0])

        total_costs = 0
        n = len(costs)//2

        for i in range(len(costs)):
            if i < n:
                total_costs += costs[i][1]
            else:
                total_costs += costs[i][0]
                
        return total_costs