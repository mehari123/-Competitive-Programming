class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        map1 = {x : -1 for x in nums1} 
        stack = []
		
        for num in nums2:
            while stack and stack[-1] < num:
                prev_num = stack.pop()
                if prev_num in map1:
                    map1[prev_num] = num
            stack.append(num)
            
        return [map1[x] for x in nums1]
                
                
            
            
        