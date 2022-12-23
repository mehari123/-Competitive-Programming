class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        size=len(nums1)
        
        index_1=m-1
        index_2=n-1
        index_3=(n+m)-1
        i=0
        while index_2>=0 and index_1>=0:
            if nums1[index_1]>=nums2[index_2]:
                nums1[index_3]=nums1[index_1]
                index_1-=1
            else:
                nums1[index_3]=nums2[index_2]
                index_2-=1
            index_3-=1
        
        while index_2>=0:
            nums1[index_3]=nums2[index_2]
            index_2-=1
            index_3-=1
            

        
        
            
            