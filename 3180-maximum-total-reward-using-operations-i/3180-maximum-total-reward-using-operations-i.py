class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        rewardValues = sorted(list(set(rewardValues)))
        x = 0
        memo = {}
        n = len(rewardValues)
        
        def f(i, x):

            if i == n:
                return x

            if (i, x) in memo:
                return memo[(i, x)]
            res = f(i + 1, x)
            if rewardValues[i] > x:
                res = max(res, f(i + 1, x + rewardValues[i]))

            memo[(i, x)] = res
            return res

        return f(0, 0)
