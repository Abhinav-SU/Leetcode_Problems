class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}

        for num in nums:
            countMap[num] = countMap.get(num,0)+1

        sorted_keys = sorted(countMap.keys(),key = lambda x : countMap[x], reverse = True)
        return sorted_keys[:k]