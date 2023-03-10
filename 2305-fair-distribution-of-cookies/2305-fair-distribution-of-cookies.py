class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        min_max = float("inf")
        cookies.sort(reverse=True)
        def distribute(index,top):
            
            nonlocal min_max
            
            if index == len(cookies):
                # index == 0
                min_max =  min(max(top),min_max)
                
                return 
            
            if min_max < max(top):
                return
            for i in range(k):
                
                top[i] += cookies[index]
                distribute(index+1,top)
                top[i] -= cookies[index]

            return
                    
        
        distribute(0,[0]*k)
        return min_max
            
        