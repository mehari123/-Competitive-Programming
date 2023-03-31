class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutuate = []
        
        def perm (nums,index,temp,visit,visit2):
            
            if  len(temp) >= len(nums):
                
                permutuate.append(temp[::])
                return 

            for i in range(len(nums)):
                
                if nums[i] < 0 and ((1 << (-1 *nums[i]) ) & visit2 ): 
                    
                    continue
                elif (nums[i] >= 0) and (1 << nums[i] ) & visit:
                    
                    continue
                
                else:
                    temp.append(nums[i])
                    
                    if nums[i] >= 0:
                        
                        visit |= (1 << nums[i])
                        
                    else:
                        
                        visit2 |= (1 << -1 * nums[i])
                        
                    perm (nums,i,temp,visit,visit2)
                    temp.pop()
                    
                    if nums[i] >= 0:
                        
                        visit &= ~(1 << nums[i])
                        
                    else:
                         visit2 &=  ~(1 << (-1 *nums[i]))
            return 
        
        
        perm (nums,0 ,[],0,0)
        
        return permutuate
            
        