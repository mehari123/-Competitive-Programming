class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        not_d = set()
        indegree = defaultdict(int)
        graph = defaultdict(list)
        
        for pre in prerequisites:
            
            graph[pre[1]].append(pre[0])
            not_d.add(pre[0])
            indegree[pre[0]] += 1
            
        independ = []
        taken_course = 0
        for i in range(numCourses):
            
            if i not in not_d:
                
                independ.append(i)
          
        
        que = deque(independ)
       
        while que:
            
            for _ in range(len(que)):
                
                q = que.popleft()
                taken_course += 1
                
                if taken_course >= numCourses:
                    
                    return True
                
                childes = graph[q]
                for chiled in childes:
                    indegree[chiled] -= 1
                    
                    if indegree[chiled] == 0:
                        
                        que.append(chiled)
                                        
        if taken_course >= numCourses:
            
            return True
        else:
            
            return False
                        
                    
        