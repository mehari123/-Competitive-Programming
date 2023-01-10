class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        ans=[]
        q_len=len(queries)
        n_len=len(nums)-1
        even=0
        
        for num in nums:
            
            if num%2==0:
                even+=num
                
        for query in queries:
            
            pre_value=nums[query[1]]
            after_query=query[0]+nums[query[1]]
            nums[query[1]]=query[0] + nums[query[1]]   
            if pre_value%2==0 and after_query%2!=0:
                even-=pre_value
            elif pre_value%2==0 and after_query%2==0:
                even-=pre_value
                even+=after_query
            elif pre_value%2!=0:
                
                if after_query%2==0:
                    even+=after_query
                    
            ans.append(even)
        return ans