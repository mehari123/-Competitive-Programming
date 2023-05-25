class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        
        new = sorted(arr)
        new[0] = 1
        index = 0
        # print(new)
        while index < len(new)-1 :
            
            if abs(new[index] - new[index+1]) > 1:
                
                new[index + 1] = new[index] + 1
            
            index += 1     
        return new[-1]