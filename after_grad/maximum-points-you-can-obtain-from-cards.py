from typing import List  

class Solution:  
    def maxScore(self, cardPoints: List[int], k: int) -> int:  
        n = len(cardPoints)  
        max_score = 0  
        
        # Calculate the sum of the first k cards (from the left)  
        current_score = sum(cardPoints[:k])  
        max_score = current_score  
        
        # Slide window to include more cards from the right  
        for i in range(k):  
            current_score = current_score - cardPoints[k - 1 - i] + cardPoints[n - 1 - i]  
            max_score = max(max_score, current_score)  
        
        return max_score