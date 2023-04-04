class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        count_of = {}
        
        for num in deck:
            
            if num in count_of:
                
                count_of[num]+= 1
            else:
                 count_of[num] = 1
        
        
        value = set(count_of.values())
        G = max(value)
        for v in value:
            
            G = math.gcd(G,v)
            
        return True if G > 1 else False
     