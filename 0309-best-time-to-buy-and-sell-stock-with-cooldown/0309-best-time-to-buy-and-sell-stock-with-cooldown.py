class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, reset = float('-inf'),float("-inf"),0

        for i in range(0,len(prices)):
            prev_hold = hold
            prev_sold = sold

            hold = max(prev_hold,reset - prices[i])
            sold = prev_hold + prices[i]
            reset = max(reset,prev_sold)

        return max(sold,reset)