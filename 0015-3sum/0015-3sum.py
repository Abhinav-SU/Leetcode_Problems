class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range (0,len(nums)-2):
            if nums[i]>0:
                return ans
            if i>0 and nums[i-1]== nums[i]:
                continue
            j,k,target=i+1,len(nums)-1,-nums[i]
            while j<k:
                current_sum =nums[j] + nums[k]
                if  current_sum == target:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif current_sum > target:
                    k-=1
                else:
                    j+=1
        return ans