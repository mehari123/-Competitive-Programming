class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        nums_dict={}
        for num in nums:
            if num in nums_dict:
                nums_dict[num]+=1
            else:
                nums_dict[num]=1
        
        good_pair=0
        for numPair in nums_dict.values():
            good_pair+=sum(i for i in range(numPair))
        
        return good_pair
        
        