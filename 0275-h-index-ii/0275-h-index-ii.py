class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        high = len( citations ) -1
        low = 0
        
        if len(citations) == 1 : return  1 if citations[0]>0 else 0
        
        while low < high :
            
            mid = ( low + high ) // 2
            
            if citations[mid] == (len(citations) - mid) :
                
                return (len(citations) - mid)
            
            if citations[mid] < (len(citations) - mid) :
                
                low = mid  + 1
                
            else:
                
                high = mid
            
    
        
        print(low,high,len(citations))
        
        return (len(citations) - high) if citations[high]>0 else 0
                
        
        