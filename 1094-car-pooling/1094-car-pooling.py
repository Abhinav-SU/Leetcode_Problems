class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events =[]
        for passenger, start,end in trips:
            events.append((start,passenger))
            events.append((end,-passenger))
        events.sort()
        cur =0
        for _,delta in events:
            cur += delta
            if cur >capacity:
                return False
        return True