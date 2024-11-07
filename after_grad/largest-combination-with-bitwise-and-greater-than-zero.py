class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        bit_counts = [0] * 24
        for number in candidates:
            
            for i in range(24):
                if number & (1 << i):  # Check if the i-th bit is set
                    bit_counts[i] += 1
        
        return max(bit_counts)





        