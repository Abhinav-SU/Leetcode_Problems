
class Solution:
    def permute(self,nums):
        num_len = len(nums)
        result = []
        if num_len == 0:
            return []
        if num_len == 1:
            return [list(nums)]

            
        def dfs(currList):
            
            if len(currList) == num_len:
                result.append(list(currList))
                return
                
            for num in nums:
                if num not in currList:
                    currList.append(num)
                    dfs(currList)
                    currList.pop()
                    
        dfs([])
        
        return result 