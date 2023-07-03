from typing import List

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        num_requests = len(requests)
        max_requests = 0
        
       
        for i in range(1 << num_requests):
            curr_requests = [0] * n
            count = 0
            

            for j in range(num_requests):
                if (i >> j) & 1:
                    curr_requests[requests[j][0]] -= 1
                    curr_requests[requests[j][1]] += 1
                    count += 1
            
           
            if all(r == 0 for r in curr_requests):
                max_requests = max(max_requests, count)
        
        return max_requests