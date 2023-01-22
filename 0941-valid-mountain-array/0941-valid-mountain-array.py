class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        peak_left=True
        peak_right=False
        
        index=1
        if len(arr)<3 or arr[0]>=arr[1] :
            return False
        elif arr[len(arr)-1]==arr[len(arr)-2]:
            return False
        while index<len(arr):
            
            if peak_left:
                
                if arr[index-1]<arr[index]:
                    pass
                elif arr[index-1]>=arr[index]:
                    peak_left=False
                    peak_right=True
            elif peak_right:
                
                
                if arr[index-1]>arr[index]:
                    pass
                elif arr[index-1]>arr[index] and index==len(arr)-1:
                    return True
                else:
                    return False
            index+=1
        return peak_right
                    