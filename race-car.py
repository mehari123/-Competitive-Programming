from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        position = deque()
        speed = deque()
        step = deque()
        visited = set()
        instruction = deque()
        
        position.append(0)
        speed.append(1)
        step.append(0)
        visited.add((0, 1))
        
        while position:
            pos, spd, stp = position.popleft(), speed.popleft(), step.popleft()
            
            if pos == target:
                return stp
            
            # Accelerate
            p1 = pos + spd
            s1 = spd * 2
            
            if (p1, s1) not in visited:
                position.append(p1)
                speed.append(s1)
                step.append(stp + 1)
                visited.add((p1, s1))
            
            # Reverse
            s2 = -1 if spd > 0 else 1
            p2 = pos
            
            if (p2, s2) not in visited:
                position.append(p2)
                speed.append(s2)
                step.append(stp + 1)
                visited.add((p2, s2))
        
      
        # return step.popleft()