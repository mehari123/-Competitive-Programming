class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        independ = set()
        visited = {}
        def dfs(i):
            
            visited[i] = False
            for node in graph[i]:
                
                if node in visited:
                    
                    if not visited[node]:
                        
                        return False
                    
                    continue
                    
                elif not dfs(node):
                    
                    visited[node] = False
                    return False
                
            visited[i] = True
            return True
        
        answer = []
        for i in range(len(graph)):
            
            if dfs(i):
                
                answer.append(i)
                
        return sorted(answer)
                
                
            
                
                
            
            