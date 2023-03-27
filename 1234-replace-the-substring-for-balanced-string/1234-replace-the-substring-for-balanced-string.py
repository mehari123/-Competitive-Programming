class Solution:
    def balancedString(self, s: str) -> int:
        n , start , count , req , cur, index , ans = len(s) , 0 ,defaultdict(int) ,[0]*4 , [0]*4 , {'Q':0,'W':1,'E':2,'R':3} , len(s)
        for i in s:count[i] += 1
        for i in count:
            if count[i] > n // 4:req[index[i]] = count[i] - n // 4
        if req == [0,0,0,0]: return 0
        for i,val in enumerate(s):
            cur[index[val]] += 1
            if cur[0] >= req[0] and cur[1] >= req[1] and cur[2] >= req[2] and cur[3] >= req[3]:
                while True:
                    if s[start] in "QWER":
                        if cur[index[s[start]]] > req[index[s[start]]]:
                            cur[index[s[start]]] -= 1
                            start += 1
                        else:
                            break
                    else:
                        start += 1
                ans = min(ans,i - start + 1)
        return ans
        
        
        
        
        
        
        
        
#         count_word = {"Q":0,"W":0,"E":0,"R":0}
#         additional_o = {}
        
#         for str1 in s:
            
#             if count_word[str1] == len(s)//4:
                
#                 if str1 in additional_o:
                    
#                     additional_o[str1] += 1
#                 else:
                    
#                     additional_o[str1] = 1
                
#             else:
                
#                 count_word[str1] += 1
        
#         if sum(additional_o.values()) == 0:
            
#             return 0
        
#         left = 0
#         min_sub = 100000
#         additional = additional_o
#         positive = additional_o
        
#         for right in range(len(s)):
            
#             # print(additional.values())
#             while sum(positive.values()) == 0:
                
#                 min_sub = min( (right - left ) , min_sub)
                
#                 if s[left] in additional :
                    
#                     additional[s[left]] +=1
                    
#                     if additional[s[left]] > 0:
                    
#                             positive[s[left]] = 1
                
#                 left += 1
                
#             if  s[right] in additional :
                
#                 additional[s[right]] -= 1
                
#                 if additional[s[right]] <= 0:
                    
#                     positive[s[right]] =0
        
#         return min_sub
            
        