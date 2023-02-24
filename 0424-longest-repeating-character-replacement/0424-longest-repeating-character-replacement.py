class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
          
            unique=set(s)
            
            max_count=0
        
            
            for s1 in unique:
                
                left=0
                count1=0
                
                for right in range(len(s)):
                    
                    if s[right]==s1:
                        
                        count1+=1
                
                    
                    while left<=right and (right-left+1)-count1>k:
                        
                        if s[left]==s1:
                            count1-=1
                        left+=1
                        
                    
                    max_count=max(right-left+1,max_count)
            
                    
            return max_count
                        
                
                
                
                
                
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         str1=[]
#         prev_str=s[0]
        
#         # print(prev_str)
#         count=0
#         str2=""
#         for str2 in s:
            
#             # print(str2)
#             if str2==prev_str:
#                 count+=1
#             else:
#                 str1.append([prev_str,count])
#                 prev_str=str2
#                 count=1
           
#         str1.append([prev_str,count])
             
#         max_sub=0
        
#         print(str1,k)
#         index=0
#         amount=k+1
#         sum1=0          
#         while index+k<len(str1):
            
#             sum1=str1[index][1]
#             for inde in range(index+1,index+k+2):
                    
#                     amount=amount-str1[inde][1]               
#                     if amount<0:
#                         break
#                     sum1+=str1[inde][1]
                    
                    
#             max_sub=max(max_sub,sum1)
                                        
#             index+=1
                        
#         return max_sub
                    
                        