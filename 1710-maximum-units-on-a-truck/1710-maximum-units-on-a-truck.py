class Solution:
	def maximumUnits(self,boxTypes,truckSize):
		
		boxTypes.sort(key=lambda x:x[1], reverse=True)
		total_units = 0
		remaining_cap = truckSize
		
		for boxes,unitPerBox in boxTypes:
			
			boxes_to_take = min(boxes,remaining_cap)
			total_units += boxes_to_take * unitPerBox
			remaining_cap -=boxes_to_take
			
			if remaining_cap ==0:
				break
		return total_units