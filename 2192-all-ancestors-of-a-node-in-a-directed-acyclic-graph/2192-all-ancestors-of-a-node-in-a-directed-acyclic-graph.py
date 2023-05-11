class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for edge in edges:
            
            graph[edge[1]].append(edge[0])
            indegree[edge[1]] += 1
        
        def bfs(i):
            
            if not graph[i]:
                
                return 
            childs = graph[i]
            
            for child in childs:
                
                if child not in visited:
                    
                    temp.append(child)
                    bfs(child)
                    visited.add(child)
                    
            return sorted(temp) if temp else temp
        
        
        ans = [[] for i in range(n)]
        # print(ans)
        for i in range(n):
            
            if i in graph:
                temp = []
                visited = set()
                ans[i] = bfs(i)
                         
        return ans
            
            
        
        