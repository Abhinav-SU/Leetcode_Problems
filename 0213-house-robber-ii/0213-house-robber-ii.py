class Solution:
    def rob(self, nums):

        n = len(nums)
        if n < 0:
            return 0
        if n == 1:
            return nums[0]

        def rob_linear(nums):
            prev1 = 0
            prev2 = 0

            for x in nums:
                res = max(x + prev2, prev1)
                prev2 = prev1
                prev1 = res

            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
