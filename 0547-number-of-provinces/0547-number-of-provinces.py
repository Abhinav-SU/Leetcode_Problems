class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        noComp = 0
        visit = [False] * size

        def dfs(i,isConnected,visit):
            visit[i] = True
            for c in range(len(isConnected)):
                if isConnected[i][c] and not visit[c]:
                    dfs(c,isConnected,visit)

        for i in range(size):
            if not visit[i]:
                noComp +=1
                dfs(i,isConnected,visit)

        return noComp


