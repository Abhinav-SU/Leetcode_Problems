
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadend_set = set(deadends)
        if '0000' in deadend_set: 
            return -1
        if '0000' == target:
            return 0
            
        q = deque()
        q.append(['0000',0])
        visited = deadend_set.copy()
        visited.add('0000')
  
        def get_directions(comboStr):
            combo =[]
            for i in range(4):
                digitFWD = (int(comboStr[i]) +1)% 10
                numFwd = comboStr[:i] + str(digitFWD) + comboStr[i+1:]
                combo.append(numFwd)
                digitBWD = (int(comboStr[i]) +10 -1)%10 
                numBWD = comboStr[:i] + str(digitBWD) + comboStr[i+1:]
                combo.append(numBWD)
                
            return combo
                
        while q:
            node,steps = q.popleft()
            
            if node == target:
                return steps
                
            for neigh in get_directions(node):
                if neigh not in visited:
                    visited.add(neigh)
                    q.append([neigh,steps+1])
                    
        return -1