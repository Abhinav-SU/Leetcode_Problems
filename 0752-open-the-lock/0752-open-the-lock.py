class Solution:
    def openLock(self,deadends,target):
        
        start ='0000'
        deadendSet = set(deadends)
        if start == target:
            return 0
        if start in deadendSet:
            return -1
            
        visited = deadendSet.copy()
        visited.add(start)
        q = deque()
        q.append((start,0))
        
        def get_neighbour(comboStr):
            neighbours =[]
            
            for i in range(4):
                
                digit = int(comboStr[i])
                
                digitFwd = str((digit+1) %10)
                neighFwd = comboStr[:i] + digitFwd + comboStr[i+1:]
                neighbours.append(neighFwd)
                
                digitBwd = str((digit -1 +10)%10)
                neighBwd = comboStr[:i] + digitBwd + comboStr[i+1:]
                neighbours.append(neighBwd)
                
            return neighbours
            
        while q:
            
            combo, turns = q.popleft()
            
            for neighbour in get_neighbour(combo):
                if neighbour not in visited:
                    if neighbour == target:
                        return turns+1
                    
        
                    visited.add(neighbour)
                    q.append((neighbour,turns+1))
                    
        return -1