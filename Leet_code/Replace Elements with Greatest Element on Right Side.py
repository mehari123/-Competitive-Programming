from itertools import islice
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        size1=len(arr)
        max_index=1
        index=0
        while index<size1 and size1>1:
            
            max_right=max(arr[max_index:])
            max_index=arr.index(max_right)
            
            # if max_index<=index:
            #     max_index=index+1
            #     max_right=max([maxi  for maxi in islice(arr,max_index,None)])
            
            for i in range(index,max_index):
                arr[i]=arr[max_index]
            
            index=max_index
            max_index+=1
            
            if max_index==size1-1:
                arr[size1-2] =arr[size1-1] 
                break
        arr[size1-1] =-1        
        return arr    
        
        
        
        
        
        
#         index1=1
#         while index1<size1:
#             max1=arr[index1]
#             index2=index1
#             while index2<size1:
                
                
#                 if max1<arr[index2]:
#                     max1=arr[index2]
#                 index2+=1
             
            
#             arr[index1-1]=max1
#             index1+=1
    
#         arr[size1-1]=-1
      
                
        
        
        
