class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        
        passangerPerKm=defaultdict(lambda:0)
        
        for trip in trips:
            
            if trip[1] in passangerPerKm:
                
                passangerPerKm[trip[1]]+=trip[0]
                
            else:
                
                passangerPerKm[trip[1]]=trip[0]
                
            if trip[2] in passangerPerKm:
                
                passangerPerKm[trip[2]]-=trip[0]
                
            else:
                
                passangerPerKm[trip[2]]=-trip[0]
         
        
        maxKm=max(passangerPerKm.keys())
        print (maxKm)
        
        pre_sum=[0]
        for index in range(maxKm):
            
            pre_sum.append(pre_sum[-1]+passangerPerKm[index])
            if pre_sum[-1]>capacity:
                
                print(pre_sum)
                return False
            
        print(pre_sum)   
        return True
            
            
                
            
                
                
        
        
        
        
        