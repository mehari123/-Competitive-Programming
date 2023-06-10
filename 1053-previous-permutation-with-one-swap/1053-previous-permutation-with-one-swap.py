class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:    
        n = len(arr)
        min_ = []
        index = []
        min_.append(arr[-1])
        index.append(n-1)
        
        for i in range(n-1,-1,-1):
            
            if min_[-1] < arr[i]:
                
                while  min_ and min_[-1] < arr[i]:

                    min_.pop()
                    inde = index.pop()
                    
                arr[inde],arr[i] = arr[i],arr[inde]
                return arr
                    
            if min_[-1] > arr[i]:
                
                min_.append(arr[i])
                index.append(i)
                
            if min_[-1] == arr[i]:
                
                min_[-1] = arr[i]
                index[-1] = i
                
              
        return arr
                
            
        
                
                
                