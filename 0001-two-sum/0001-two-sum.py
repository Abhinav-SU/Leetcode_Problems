class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #the idea is to have two such number from nums array that they result in target
        #to do so we need a hash,map and for eaxch element starting first index we try to find if the target - nums[index] is already present in our hashmap if so we return the asnwre as we also store the index in that hashmap

        numsMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numsMap:
                return [numsMap[complement],i]
            numsMap[nums[i]] = i
        return []