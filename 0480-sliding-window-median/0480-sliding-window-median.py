class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        small = []
        large = []
        deleted = defaultdict(int)
        result =[]

        def balance_heap():
            while len(small) > len(large)+1:
                heapq.heappush(large, -heapq.heappop(small))
            while len(large) > len(small):
                heapq.heappush(small,-heapq.heappop(large))

        def prune(heap,is_small):
            while heap:
                val = - heap[0] if is_small else heap[0]
                if deleted[val] > 0:
                    deleted[val] -= 1
                    heapq.heappop(heap)
                else:
                    break

        for i in range(k):
            heapq.heappush(small,-nums[i])
        balance_heap()

        if k % 2==1:
            result.append(-small[0])
        else:
            result.append((-small[0] + large[0])/2)

        for i in range(k,len(nums)):
            out_num = nums[i-k]
            in_num = nums[i]


            deleted[out_num] += 1
            balance =0

            if out_num <= -small[0]:
                balance -= 1
            else:
                balance += 1
            
            if len(small) > 0 and in_num <= -small[0]:
                heapq.heappush(small,-in_num)
                balance += 1
            else:
                heapq.heappush(large,in_num)
                balance -= 1

            if balance < 0:
                heapq.heappush(small, -heapq.heappop(large))
            elif balance >0:
                heapq.heappush(large, -heapq.heappop(small))

            prune(small,True)
            prune(large,False)

            if k % 2 == 1:
                result.append(-small[0])
            else:
                result.append((-small[0]+large[0])/2)
		
        return result           
