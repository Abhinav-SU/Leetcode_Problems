class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:



        def findOriginal(original):
            for i in range(len(nums)):
                if nums[i]==original:
                    original = original * 2
                else: 
                    continue
            return original
        
        for i in range(len(nums)):
            original = findOriginal(original)
        
        return original