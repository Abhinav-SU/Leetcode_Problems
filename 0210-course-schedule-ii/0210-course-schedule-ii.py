class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = defaultdict(list)

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] +=1

        q = deque(i for i in range(numCourses) if indeg[i] ==0)
        res =[]
        count =0

        while q:
            cur_course = q.popleft()
            res.append(cur_course)
            count+=1
            for nxt in graph[cur_course]:
                indeg[nxt] -=1
                if indeg[nxt]==0:
                    q.append(nxt)
        
        return res if count == numCourses else []