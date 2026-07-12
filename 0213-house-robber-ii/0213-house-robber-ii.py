class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 0:
            return 0
        if ln == 1:
            return nums[0]

        def robCircle(arr: List[int]) -> int:

            if len(arr) == 1:
                return arr[0]
            prev2 = arr[0]
            prev = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                take = arr[i] + prev2
                not_take = 0 + prev
                curi = max(take, not_take)
                prev2 = prev
                prev = curi
            return prev

        return max(robCircle(nums[1:]), robCircle(nums[:-1]))
