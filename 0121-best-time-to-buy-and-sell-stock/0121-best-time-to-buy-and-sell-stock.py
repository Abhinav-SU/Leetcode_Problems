class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float("inf")
        maxProfit = 0

        for price in prices:

            if price < lowest:
                lowest = price

            elif price - lowest > maxProfit:
                maxProfit = price - lowest
        return maxProfit
