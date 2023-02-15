class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums))
        cmp = lambda x, y: ((x+y) > (y+x)) - ((x+y) < (y+x))
        nums = sorted(nums, key=cmp_to_key(cmp))
        return str(int(''.join(nums[::-1])))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         str1=[]
#         str2=[]
#         str3=[]
        
#         for index,num in enumerate(nums):
#             str0=str(num)
#             str1.append([int(str0[0]),index])
            
#             if len(str0)>1:
#                 str2.append([int(str0[1]),index])
#             else:
#                 str2.append([0,index])
#             if len(str0)>2:
#                 str3.append([int(str0[2]),index])
#             else:
#                 str3.append([0,index])
#         str1.sort()
#         str2.sort()
#         str3.sort()
        
#         pointer1=0
#         pointer2=1
#         pointer3=1
#         ans=""
#         while pointer2<len(nums):
#             if str1[pointer1][0]<str1[pointer2][0]:
                
#                 ans+=str(nums[str1[pointer1][1]])
#                 pointer1=pointer2
#                 pointer2+=1
#                 pointer3=pointer2
               
#             elif str1[pointer1][0]==str1[pointer2][0]:
                
#                 if str2[pointer1][0]<str2[pointer2][0]:
#                     ans+=str(nums[str2[pointer1][1]])
#                     pointer1=pointer2
#                     pointer2+=1
#                     pointer3+=pointer2
                
#                 elif str2[pointer1][0]==str2[pointer2][0]:
#                         ans+=str(nums[str3[pointer1][1]])
#                         pointer1=pointer2
#                         pointer2+=1
#                         pointer3+=pointer2
#         return str1
        
                             
            
            
                        
                        
                        
                        
                        
        
            
        