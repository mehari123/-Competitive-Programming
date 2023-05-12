class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for rich in richer:
            
            graph[rich[0]].append(rich[1])
            indegree[rich[1]] += 1
        
        que = deque()
       
        for i in range(len(quiet)):
            
            if i not in indegree:
                
                que.append(i)
                
        ans = [i for i in range(len(quiet))]
        while que:
            
            parent = que.popleft()
            childs = graph[parent]
            
            for child in childs:
                
                indegree[child] -= 1
                # print(child,parent,quiet[child],quiet[parent])
                
                if quiet[child] >= quiet[parent]:
                    
                    ans[child] = ans[parent]
                    quiet[child] = quiet[parent]
                    
                 
                if indegree[child] == 0:
                    
                    que.append(child)
                    
                    
        return ans
            