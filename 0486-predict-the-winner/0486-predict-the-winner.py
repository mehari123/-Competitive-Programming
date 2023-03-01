class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        def Predict(left,right,p1_turn):
            
            if left==right:
                
                if p1_turn:
                    
                    return [nums[left],0]
                else:
                    
                    return [0,nums[left]]
                
            ans1=[0,0]
            ans2=[0,0]
            
            if p1_turn:
                
                lresult=Predict(left+1,right,False)
                ans1[0]+= nums[left]
                ans1[0] += lresult[0]
                ans1[1]+=lresult[1]
                rresult=Predict(left,right-1,False)
                
                ans2[0]+=nums[right]+rresult[0]
                ans2[1]+=rresult[1]
                
                if ans1[0]>=ans2[0]:
                    return ans1
                else:
                    return ans2
                
            else:
                
                lresult=Predict(left+1,right,True)
                ans1[1]+= nums[left]+lresult[1]
                ans1[0]+=lresult[0]
                
                rresult=Predict(left,right-1,True)
                
                ans2[1]+=nums[right]+rresult[1]
                ans2[0]+=rresult[0]
                
                if ans1[1]>=ans2[1]:
                    return ans1
                else:
                    return ans2
                
            
        result=Predict(0,len(nums)-1,True)
        
        if result[0]>=result[1]:
            return True
        else:
            return False
        
        
        