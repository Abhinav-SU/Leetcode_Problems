class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        node_len = len(graph)

        result =[]

        if node_len ==0:
            return []
        if len == 1:
            return [[0]]

        def dfs(currentNode,currentPath):
            if currentNode == node_len-1:
                result.append(list(currentPath))

            
			
            for neighbour in graph[currentNode]:
                currentPath.append(neighbour)
                dfs(neighbour,currentPath)
            currentPath.pop()	
			

		
        dfs(0,[0])
        return result