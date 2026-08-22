class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostK(nums,k) - self.atmostK(nums,k-1)
    def atmostK(self,nums,X):
        frq = defaultdict(int)
        left = 0
        count =0
        for right in range(len(nums)):
            frq[nums[right]] +=1
            while len(frq) > X:
                frq[nums[left]] -=1
                if frq[nums[left]] ==0:
                    del frq[nums[left]]
                left+=1
            count += right -left +1
        return count 