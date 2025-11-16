class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph =defaultdict(list)
        indegree = [0] * numCourses
        for post,pre in prerequisites:
            graph[pre].append(post)
            indegree[post] +=1

        q = deque()
        q.extend(([i for i in range(numCourses) if indegree[i] == 0]))
        result = []

        while q:

            course = q.popleft()
            result.append(course)

            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei]==0:
                    q.append(nei)

        if len(result) == numCourses:
            return result
        else:
            # A cycle exists, meaning not all courses could be taken.
            return []