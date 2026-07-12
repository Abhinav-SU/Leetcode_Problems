class Solution:
    def rob(self, nums: List[int]) -> int:
        ln = len(nums)
        if ln == 0:
            return 0
        if ln == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            take = nums[i] + prev2
            not_take = 0 + prev
            curi = max(take, not_take)
            prev2 = prev
            prev = curi
        return prev
