class Solution:
    def findOrder(self,numCourses,preprequisites):

            
        adjList = defaultdict(list)
        indegree = [0]*numCourses
        for course, prereq in preprequisites:
            adjList[prereq].append(course)
            indegree[course] +=1
        order = []
        queue = deque(course for course in range(numCourses) if indegree[course]==0)
        while queue:
            curCourse = queue.popleft()
            order.append(curCourse)
            for nei in adjList[curCourse]:
                indegree[nei] -=1
                if indegree[nei]==0:
                    queue.append(nei)
        if len(order) == numCourses:
            return order
        return []