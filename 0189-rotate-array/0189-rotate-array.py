class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        size=len(nums)
        new_k=k%size
        right=len(nums)-new_k
        
        ans=[]
        for num in nums:
            ans.append(num)
        index=0
        
        while right<size:
            
            nums[index]=ans[right%size]
            right+=1
            index+=1
        index=new_k  
        while left<(len(nums)-new_k):
            nums[index%size]=ans[left%size]
            left+=1
            index+=1
        
            