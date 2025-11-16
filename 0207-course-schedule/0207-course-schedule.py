class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create graph #initialize indegree 
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u,v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque()
        q.extend([i for i in range(numCourses) if indegree[i] == 0])
        #add each node of the graph and check for the node where indegree is 0 
        #add that to the queue 
        completed_course = 0
        #while a node exist in our queue
        while q:
            #pop out the queue elem
            curr_course = q.popleft()
            #append the node to result 
            completed_course +=1
            #now we backtrack to nodes that are connected to this node 
            for v in graph[curr_course]:
                indegree[v] -=1
            # decreaese their indegree by 1 
                if indegree[v] == 0:
                    q.append(v)
            #check that decreased indegree is 0 then add to the queue

        #check if the final result is not = to n if so return false 
        #else return true
        return completed_course == numCourses