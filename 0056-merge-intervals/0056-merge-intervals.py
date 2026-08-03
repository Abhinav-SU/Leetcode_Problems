class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            lastMerged = merged[-1]

            if current[0] <= lastMerged[1]:
                lastMerged[1] = max(current[1],lastMerged[1])
            else:
                merged.append(current)
        return merged