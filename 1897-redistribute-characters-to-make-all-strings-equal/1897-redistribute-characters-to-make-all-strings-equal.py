class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        letter_map = defaultdict(int)
        
        for word in words:
            
            for letter in word:
                
                letter_map[letter] += 1
                
                
        length = len(words)
        
        for key,value in letter_map.items():
            
            if (value % length) != 0:
                
                return False
            
        return True
            
            