class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times = times
        self.Persons = []
        max1=0
        p=persons[0]
        T=defaultdict(lambda:0)
        for person in persons:
            
            if person in T:
                
                T[person]+=1
            else:
                
                T[person]=1
            
            if max1 <= T[person]:
                
                max1 = T[person]
                p = person   
                  
            self.Persons.append(p)
            
    

    def q(self, t: int) -> int:
        
        high = len(self.times)
        low = 0
        ans = 0
        mid=0
        while low < high :
            
            mid = ( high + low ) // 2
            
            if  self.times[mid] > t :
                
                high = mid
                
            else:
                
                low = mid + 1
                ans = mid
                
        # print(ans,low,high)
        return self.Persons[ans]
                
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)