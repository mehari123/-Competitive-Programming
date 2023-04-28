class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        bomb_list = [i for i in range(len(bombs))]
        bombs2 = defaultdict(set)
        bombs_ = defaultdict(set)
        bomb_graph = defaultdict(set)
   
        
        for index,bomb in enumerate(bombs):
            
            bombs_[index]=bomb
            bomb_graph[index]=set()
        
        for b in bomb_list:
            
            value = bombs_[b]
            x1 = value[0]
            y1 = value[1]
            r1 = value[2]
        
            for b2 in bomb_list:
                
                if b != b2:
                    
                    value2 = bombs_[b2]
                    x2 = value2[0]
                    y2 = value2[1]
                    r2 = value2[2]
                    
                  
                    if math.sqrt((((x2-x1)**2) + ((y2-y1)**2))) <= r1:

                        bomb_graph[b].add(b2)

                    if math.sqrt((((x2-x1)**2) + ((y2-y1)**2) )) <= r2:

                        bomb_graph[b2].add(b)
            
         
                
        def detonate(key):
            
            nonlocal curr
            de = bomb_graph[key]
            visited.add(key)
            curr += 1
            
            for d in de:
                
                if d in bomb_graph and d not in visited:
                    
                    detonate(d)

                    
            
               
        max_ = 0
        
        for bomb in bomb_list:
            
            curr = 0
            visited = set()
            detonate(bomb)
            max_ = max(max_,curr)
            
        return max_
                
        