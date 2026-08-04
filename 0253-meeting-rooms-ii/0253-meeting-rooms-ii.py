class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start,end in intervals:
            events.append((start,1))
            events.append((end,-1))
        events.sort()
        cur = best =0
        for _, delta in events:
            cur +=delta
            best = max(best,cur)
        return best