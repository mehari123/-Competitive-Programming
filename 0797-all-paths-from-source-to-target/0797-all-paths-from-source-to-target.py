class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        
        def dfs(from1,to,path):
            
            if to == len(graph) -1:
                
                path.append(to)
                result.append(path[::])
                
                return 
            
            path.append(to)
            
            for i,to in enumerate(from1):
                
                dfs(graph[to],to,path)
                path.pop()
                
        
        dfs(graph[0],0,[])
        return result