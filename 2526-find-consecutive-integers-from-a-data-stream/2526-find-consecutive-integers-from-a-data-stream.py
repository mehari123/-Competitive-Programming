class DataStream:

    def __init__(self, value: int, k: int):
        
        self.value=value
        self.k=k
        self.index=0
        self.que=[]
        

    def consec(self, num: int) -> bool:
        
        self.que.append(num)
        if len(self.que)>=self.k:
            
            if self.que[-1]!=self.value:
                
                self.index=len(self.que)
                
                
            if len(self.que)-self.index==self.k:
                    self.index+=1 
                    return True
            # print(len(self.que),self.index)
            return False
            
        else:
            
            if self.que[-1]!=self.value:
                
                self.index=len(self.que)
                 
            return False
        
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)