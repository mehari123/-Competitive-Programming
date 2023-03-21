class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        
        pos_s = []
        
        for pos, spe in zip(position,speed):
            
            pos_s.append([pos,spe])
            
        pos_s.sort()
        time = []
        
        for pos in pos_s:
            
            time.append((target-pos[0])/pos[1])
            
        stack = []
        
        for t in time:
            
            while stack and stack[-1] <= t:
                
                stack.pop()
                
            stack.append(t)
        
        return len(stack)
            
                
        
        
        