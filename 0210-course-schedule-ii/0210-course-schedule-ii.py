class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses
        graph = defaultdict(list)

        for course,prereq in prerequisites:
            graph[prereq].append(course)
            indeg[course] +=1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        count = 0
        order = []
        while q:
            curr_course = q.popleft()
            count +=1
            order.append(curr_course)
            for nxt in graph[curr_course]:
                indeg[nxt] -=1
                if indeg[nxt] == 0:
                    q.append(nxt)

        return order if numCourses == count else []
