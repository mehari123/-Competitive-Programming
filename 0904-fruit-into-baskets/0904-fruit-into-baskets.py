class Solution:
       def totalFruit(self, tree: List[int]) -> int:
            
            fruits=defaultdict(lambda:0)
            left=0
            max_f=0
           
            for right in range(len(tree)):
                
                while len(fruits)>2:
                    
                    fruits[tree[left]]-=1
                    if  fruits[tree[left]]==0:
                        
                        del  fruits[tree[left]]
                        
                    left+=1
                    
                fruits[tree[right]]+=1
                
                if len(fruits)<=2:
                    
                    max_f=max(sum(fruits.values()),max_f)  
            
            return max_f
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
#                 if len(fruits)==2:
                        
#                     if tree[right] in fruits:
                            
#                             fruits[tree[right]]+=1
#                             max_f=max(sum(fruits.values()),max_f)
#                             right+=1
#                             continue
#                     else:
                        
#                         max_f=max(sum(fruits.values()),max_f)    
#                         temp=left+fruits[tree[left]]
#                         fruits[tree[left]]-=1
                        
#                         if fruits[tree[left]]==0:
#                             del fruits[tree[left]]
#                         else:
#                             value=fruits[tree[right-1]]
#                             fruits.clear()
#                             fruits[tree[right-1]]=value
#                             # fruits[tree[right-1]]+=1
#                         left=temp
                        
#                 fruits[tree[right]]+=1  
#                 max_f=max(sum(fruits.values()),max_f)
#                 right+=1
#                 print(fruits)   
#             return max_f
                    
                
                
                
                
       
        