from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        total_c = 0
        sortted = SortedList()
        
        for num in instructions: 
            
            total_c += min(sortted.bisect_left(num),len(sortted)-sortted.bisect_right(num))
            sortted.add(num)
            total_c %=(10**9+7)

        return total_c
       