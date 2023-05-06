class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        frequency = defaultdict(int)
        
        for word in words:
            frequency[word] += 1
        
        heap = []
        
        for word, freq in frequency.items():
            heappush(heap, (-freq, word))
        
        ans = []
        while k > 0:
            freq, word = heappop(heap)
            ans.append(word)
            k -= 1
        
        return ans
