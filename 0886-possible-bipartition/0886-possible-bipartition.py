class Solution:
    def possibleBipartition(self, k: int, dislikes: List[List[int]]) -> bool:
        
        adjecency = defaultdict(set)
        
        for dis in dislikes:
            
            adjecency[dis[0]].add(dis[1])
            adjecency[dis[1]].add(dis[0])
            
        color = [-1] * k
        
        def dfs(node):    
            
            for n in adjecency[node]:
                
                if color[n-1] == color[node-1]:
                    
                    return False
                
                elif color[n-1] == -1:
                    
                    if color[node-1] == 1:
                        
                        color[n-1] = 0
                        
                    else:
                        
                        color[n-1] = 1
                    
                    if not dfs(n):
                        
                        return False
                
            return True
                    
            
        for i in range(1, len(adjecency)+1):
            
            if color[i-1] == -1 :
                
                color[i-1] = 1
                
                if not dfs(i):
                    
                    return False
                
        return True
     