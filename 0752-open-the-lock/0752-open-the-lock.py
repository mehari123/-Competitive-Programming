class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visit = set(deadends)
        if '0000' in visit:
            
            return -1
        
        if target == '0000':
            return 0

        visit.add('0000')
        que = deque(['0000'])
        level = 0
        
        while que:
            
            level += 1
            for _ in range(len(que)):
                
                key = list(map(int, que.popleft()))
                for i in range(4):
                    
                    key[i] = (key[i] + 1) % 10
                    lock = ''.join(map(str,key))
                    if lock not in visit:
                        
                        que.append(lock)
                        visit.add(lock)
                    
                    if target == lock:
                        return level
                    
                    key[i] = (key[i]-2) % 10
                    lock = ''.join(map(str, key))
                    if lock not in visit:
                        
                        que.append(lock)
                        visit.add(lock)
                    
                    if target == lock:
                        return level

                    key[i] = (key[i]+1) % 10


        return -1