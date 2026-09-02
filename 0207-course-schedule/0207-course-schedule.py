class Solution:
    def canFinish(self,numCourses,prerequisites):
        if not prerequisites:
            return True
        adjList = defaultdict(list)
        indegree = [0]*numCourses
        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] +=1
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        count = 0
        while queue:
            curCourse = queue.popleft()
            count+=1
            for nei in adjList[curCourse]:
                indegree[nei] -=1
                if indegree[nei]== 0:
                    queue.append(nei)
        return count == numCourses