class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        graph = defaultdict(int)
        rank = defaultdict(int)
        for k in range(len(source)):
            
            graph[k] = k
            rank[k] = 1
            
        def find(x):

            if x != graph[x]:

                graph[x] = find(graph[x])

            return graph[x]
        
        def union(i,j):
            
            root1 = find(i)
            root2 = find(j)
            if root1 != root2:
                
                if rank[root2] > rank[root1]:

                    temp = root1
                    root1 = root2
                    root2 = temp
    
                rank[root1] += rank[root2]
                graph[root1] = root2
                
        for i,j in allowedSwaps: union(i,j)
        counter = defaultdict(Counter)
        for index in range(len(source)):

            counter[find(index)][source[index]] += 1

        haming = 0
        for ind in range(len(target)):

            if counter[find(ind)][target[ind]] > 0 :

                counter[find(ind)][target[ind]] -= 1

            else:
                
                haming += 1

        return haming