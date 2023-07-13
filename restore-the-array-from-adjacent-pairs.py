class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for adj in adjacentPairs:
            
            u,v = adj
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
            
        que = deque()
        visited = set()
        ans = []
        for key,value in graph.items():
            
            # print(key,value,len(value))
            if len(value) == 1:
                
                que.append(key)
                ans.append(key)
                visited.add(key)
                break
         
        # print(graph)
        
        while que:
            
            parent = que.popleft()
            
            childs = graph[parent]
            # print(parent,childs)
            for child in childs:
                
                indegree[child] -= 1
                if indegree[child] == 1:
                    
                    ans.append(child)
                    que.append(child)
                if indegree[child] == 0 and child not in visited:
                    
                    ans.append(child)
                    
                visited.add(child)
                    
                    
        return ans