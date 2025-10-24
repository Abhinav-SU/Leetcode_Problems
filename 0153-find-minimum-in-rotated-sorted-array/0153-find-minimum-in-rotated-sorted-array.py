class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high =len(nums)-1
        currMin=0
        while low < high:
            mid = low + (high-low)//2
            currMin = nums[mid]
            if nums[low] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return min(currMin,nums[low])
