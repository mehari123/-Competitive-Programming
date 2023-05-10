class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        indegree = defaultdict(int)
        graph2 = defaultdict(list)
        independ = set()
        
        for index,g in enumerate(graph):
            
            for i in g:
                
                graph2[i].append(index)
                independ.add(index)
                indegree[index] += 1
                
        independent = []
        for i in range(len(graph)):
            
            if i not in independ:
                
                independent.append(i)
                
        
        que = deque(independent)
        ans = []
        while que:
            
            for _ in range(len(que)):
                
                q = que.popleft()
                ans.append(q)
                childes = graph2[q]
                for child in childes:
                    
                    indegree[child] -= 1
                    
                    if indegree[child] == 0:
                        
                        que.append(child)
                        
        return sorted(ans)
                
                
            
                
                
            
            