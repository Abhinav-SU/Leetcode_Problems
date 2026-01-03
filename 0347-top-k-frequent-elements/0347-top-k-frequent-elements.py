#tok K frequent elem
from collections import Counter
import heapq
class Solution:
	def topKFrequent(self,nums,k):
		count = Counter(nums)
		
		minHeap = []
		
		for key,freq in count.items():
			heapq.heappush(minHeap,(freq,key))
			
			if len(minHeap) > k:
				heapq.heappop(minHeap)
				
		return [val for freq,val in minHeap]