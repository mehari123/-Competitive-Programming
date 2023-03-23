class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

            ans = []
            if len(nums1) >= len(nums2):
                
                nums3 = nums1
                nums4 = nums2 
            else:
                
                nums3 = nums2
                nums4 = nums1
        
        
            
            nums3.sort()
            
            nums4 = nums4
           
            
            #if len(nums3) == 1 and nums3[0] == nums4[0]:
                
               # ans.append(nums1[0])
                
            for num in nums4:
                
                high = len(nums3) -1
                low = 0
                while low <= high:
                    
                    mid = (high + low ) //2
                    if nums3[mid] > num:
                        high = mid - 1
                    elif nums3[mid] < num:
                        
                        low = mid + 1
                    else:
                        
                        ans.append(num)
                        nums3.remove(num)
                        break
                        
            print(ans,nums3,nums4)
            return ans
                    
                
        
                
                
        
        
        