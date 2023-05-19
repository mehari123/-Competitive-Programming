class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        graph = defaultdict(int)
        rank = defaultdict(int)
        
        for ch in range(26):
            
            graph[chr(97 + ch)] = chr(97+ch)
            rank[chr(97+ch)] = ch
        
        
        
        def root_find(x):
            
            if x in graph and graph[x] == x:
                
                return x
            
            root = root_find(graph[x])
            graph[x] = root
            return root
        
        for ch1,ch2 in zip(s1,s2):
            
            root1 = root_find(ch1)
            root2 = root_find(ch2)
            
            if root1 != root2:
                
                if rank[root1] < rank[root2]:
                    
                    graph[root2] = graph[root1]
                    # rank[root1] += rank[root2]
                    
                else:
                    
                    graph[root1] = graph[root2]
                    # rank[root2] += rank[root1]
                    
        ans = ""
        
        for c in baseStr:
            
            ans += root_find(c)
            
        return ans
                
                
            
            
            
        