class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        adjecency = defaultdict(set)
        count1 = defaultdict(int)
        for road in roads:
            
            adjecency[road[0]].add(road[1])
            adjecency[road[1]].add(road[0])
            count1[road[0]] += 1
            count1[road[1]] += 1
            
            
                
            
        max_ = float("-inf")
        for key in range(n):
            
            for key2 in range(n):
                
                if key == key2:
                    continue
                
                if key in adjecency[key2]:
                    
                    max_ = max(max_,count1[key] + count1[key2] -1)
                    
                else:
                    max_ = max(max_,count1[key] + count1[key2]) 
                    
       
            
        return max_
                
                