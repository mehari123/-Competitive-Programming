class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        keys = deque()
        keys.append(0)
        visited = set()
        visited.add(0)
        def bfs(keys):
            
            if not keys:
                return
            next_ = keys.popleft()
            room = rooms[next_]
            
            for r in room:
                
                if r not in visited:
                    visited.add(r)
                    keys.append(r)
                    
            bfs(keys)
        
        
        bfs(keys)
        for room in range(len(rooms)):
            
            if room not in visited:
                
                return False
            
        return True
            
            
            
            
            
        