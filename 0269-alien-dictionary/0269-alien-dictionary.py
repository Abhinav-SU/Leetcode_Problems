class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        indegree = {c:0 for c in adj}

        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    u,v = w1[j],w2[j]
                    if v not in adj[u]:
                        adj[u].add(v)
                        indegree[v] +=1
                    break

        q  = deque([c for c in indegree if indegree[c]==0])
        order = []

        while q:
            u = q.popleft()
            order.append(u)

            for v in adj[u]:
                indegree[v] -=1
                if indegree[v] == 0:
                    q.append(v)

        return "".join(order) if len(order) == len(indegree) else ""
