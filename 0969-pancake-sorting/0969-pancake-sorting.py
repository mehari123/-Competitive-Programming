class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        result=[]
        index=len(arr)
       
        while index>0:
            flipd=max(arr[:index])
            flipd_index=arr.index(flipd)
            if flipd_index!=0:
                result.append(flipd_index+1)
               
            arr[:flipd_index+1]= arr[:flipd_index+1][::-1]
            arr[:index]= arr[:index][::-1]
            
            result.append(index)
            index-=1
            
        return result
      
            
        