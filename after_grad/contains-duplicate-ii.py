class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        same_ = defaultdict(list)

        for i,j in enumerate(nums):

            same_[j].append(i)

        for key,value in same_.items():

            if len(value) > 1:
                value.sort()

            for i in range(len(value)-1):

                if (value[i+1] - value[i]) <= k:

                    return True
        
        return False




        