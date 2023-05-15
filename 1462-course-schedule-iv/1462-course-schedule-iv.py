class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        graph = defaultdict(list)
        
        for pre in prerequisites:
            
            graph[pre[0]].append(pre[1])
         
        def is_prime(p):
        
            while que:

                parent = que.popleft()
                childes = graph[parent]

                if  parent not in graph:

                    return False

                for child in childes:

                    if child == p:

                        return True
                    
                    elif child not in visited:
                        
                        que.append(child)
                    
                    visited.add(child)
                    
        ans = []           
        for query in queries:
            
            visited = set()
            que = deque()
            que.append(query[0])
            
            if is_prime(query[1]):
                
                ans.append(True)
                
            else:
                
                ans.append(False)
                
        return ans
            
            
            
            
        