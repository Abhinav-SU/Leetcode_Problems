class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = float("inf")

        for price in prices:
            if price <  minVal:
                minVal = price
            maxProfit = max(maxProfit,price-minVal)
        return maxProfit