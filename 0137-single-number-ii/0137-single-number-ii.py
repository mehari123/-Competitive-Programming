class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       
        non_reapted, reapted = 0, 0

        for i in nums:

            reapted |= (non_reapted & i)  
            non_reapted ^= i

            shared = (non_reapted & reapted)  
            non_reapted ^= shared
            reapted ^= shared

        return non_reapted
                    
                    
                