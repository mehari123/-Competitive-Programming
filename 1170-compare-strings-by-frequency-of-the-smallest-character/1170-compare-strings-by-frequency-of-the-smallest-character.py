class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def count_frequency(words):
            
            counted = []
        
            for word in words:
                
                count1 = Counter(list(word))
        
                for index in range(97,123):
                    
                    if chr(index) in count1:
                        
                        counted.append(count1[chr(index)])
                        
                        break
                        
            return counted
  
        queries = count_frequency(queries)
        words = count_frequency(words)
        words=sorted(words)
        ans = []
        
        for query in queries:
            
            high = len(words)-1
            low = 0
            A=high
            
            while  low <= high :
                
                mid = ( low + high ) // 2
                
                if words[mid] > query :
                   
                    high = mid - 1
                    
                else:
                    
                    low = mid+1
                    A = low
                    
            ans.append(len(words)-A)
            
        return ans
            
                
        