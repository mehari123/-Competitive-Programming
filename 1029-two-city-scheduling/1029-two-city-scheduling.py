class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        
        p = defaultdict(int)
        
        for index,c in enumerate(costs):
            
            p[index] = (c[0] - c[1])
            
        p = sorted(p.items(), key=lambda x: abs(x[1]),reverse = True)
        
        n = len(costs)
        cityA,cityB,min_c = 0, 0, 0
        
        for index,diff in p:
            
            if cityA < n//2 and cityB < n//2:
                
                
                if diff >= 0 :

                    cityA += 1
                    min_c += min(costs[index])

                else:

                    cityB += 1
                    min_c += min(costs[index])
                    
            elif cityA < n//2 and cityB >= n//2:
                
                if diff >= 0:

                    cityA += 1
                    min_c += min(costs[index])

                else:

                    cityB += 1
                    min_c += max(costs[index])
                    
            else:
                
                if diff >= 0:

                    cityA += 1
                    min_c += max(costs[index])
                    
                else:

                    cityB += 1
                    min_c += min(costs[index])
                
        return min_c
                

        
        
        