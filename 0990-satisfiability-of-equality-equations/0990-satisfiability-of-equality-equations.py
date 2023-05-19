class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        
        graph = defaultdict(int)
        rank = defaultdict(int)
        not_e = []
        for ch in range(26):
            
            graph[chr(97 + ch)] = chr(97+ch)
            rank[chr(97+ch)] = ch
        
        
        
        def root_find(x):
            
            if x in graph and graph[x] == x:
                
                return x
            
            root = root_find(graph[x])
            graph[x] = root
            return root
        
        for c1,c2,c3,c4 in equations:
            
            root1 = root_find(c1)
            root2 = root_find(c4)
            
            if c2 == "=":
                
                if root1 != root2:

                    if rank[root1] < rank[root2]:

                        graph[root2] = graph[root1]
                        # rank[root1] += rank[root2]

                    else:

                        graph[root1] = graph[root2]
                        # rank[root2] += rank[root1]
            else:
                
                if root1 == root2:
                    
                    return False
                else:
                    not_e.append([root1,root2])
        
        # print(not_e)
        for x,y in not_e:
            
            root1 = root_find(x)
            root2 = root_find(y)
            if root1 == root2:
                
                return False
            
        return True
                