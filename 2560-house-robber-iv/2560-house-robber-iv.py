class Solution:
    def minCapability(self, nums, k):
        def canRob(cap):
            count, i, n = 0, 0, len(nums)

            while i < n:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        lo, hi = min(nums), max(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if canRob(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
