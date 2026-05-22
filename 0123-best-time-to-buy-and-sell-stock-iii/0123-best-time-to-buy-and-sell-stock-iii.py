class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1buy = float("inf")
        t2buy = float("inf")
        t1profit = 0
        t2profit = 0

        for price in prices:
            # First transaction
            # t1buy: smallest price to buy for the first transaction
            t1buy = min(t1buy, price)
            # t1profit: maximum profit from the first transaction
            # (current price - cost of first buy)
            t1profit = max(t1profit, price - t1buy)
            
            # Second transaction
            # t2buy: smallest price to buy for the second transaction,
            # adjusted by the profit from the first transaction
            # (current price - t1profit already made)
            t2buy = min(t2buy, price - t1profit)
            # t2profit: maximum profit from two transactions
            # (current price - cost of second buy, considering t1profit)
            t2profit = max(t2profit, price - t2buy)
            
        return t2profit