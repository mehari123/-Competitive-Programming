class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        words = set(words)
        bit_mask = []
        
        for word in words:
            mask = 0
            for char in word:
                
                mask |= 1 << (ord(char) - ord("a"))
            
            bit_mask.append(mask)
            
        max_word = 0
        
        for i ,(word,mask) in enumerate(zip(words,bit_mask)):
            
            for j, (word2,mask2) in enumerate(zip(words,bit_mask),start = 1):
                
                if mask & mask2 == 0:
                    
                    max_word = max(max_word, len(word) * len(word2))
                    
        return max_word
                
            
    
        