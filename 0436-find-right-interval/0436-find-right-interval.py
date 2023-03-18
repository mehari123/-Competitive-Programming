class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        starts = defaultdict(lambda:-1)
        start_list=[]
        ans = []
        for index,interval in enumerate(intervals):
            
            starts[interval[0]]=index
            start_list.append(interval[0])
            
            
        start_list.sort()
        start_list.append(float("inf"))
        for interval in intervals:
            
            high = len(start_list)
            low = 0
            starter = high
            
            while low <= high:
                
                mid = (high + low) // 2
               
                if mid == len(start_list):
                    
                    break
    
                if  start_list[mid] > interval[1]:
                    
                    starter = mid
                    high = mid -1 
                    
                elif start_list[mid] == interval[1]:
                    starter = mid
                    break
                else:
                    
                    low = mid +1
                    
            ans.append(starts[start_list[starter]])
        
        return ans
            
                    
            
            
            
            
        
        