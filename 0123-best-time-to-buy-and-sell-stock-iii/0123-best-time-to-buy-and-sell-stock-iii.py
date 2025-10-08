class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1buy = float("inf")
        t2buy = float("inf")
        t1profit =0
        t2profit=0

        for price in prices:
            t1buy = min(t1buy,price)
            t1profit = max(t1profit, price-t1buy)
            t2buy = min(t2buy, price-t1profit)
            t2profit =max(t2profit,price-t2buy)

        return t2profit
        