class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        high = sum(weights)
        low = max(weights)
        
        while low < high:
            
            mid = (high + low) // 2
            sum1=0
            index = 0
            day = 1
            
            while index < len(weights):
                
                
                sum1 += weights[index]
                index += 1
                
                if  sum1 > mid :
                    
                    sum1 = weights[index-1]
                    day += 1
                    # continue
                   
                    
                
            if day <= days :
                
                high = mid
                
            else:
                
                low = mid+1
                
        return high
                
                    
                
                
                
            
            
            