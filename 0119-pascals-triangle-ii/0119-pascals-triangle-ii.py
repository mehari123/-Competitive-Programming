class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def getP(self, rowIndex: int,pascal) -> List[int]:
            
            if rowIndex==0:
            
                return pascal
        
            pascal1=[1]
            for index in range(len(pascal)-1):
            
                pascal1.append(pascal[index]+pascal[index+1])
            
            pascal1.append(1)
            
        
            return getP(self,rowIndex-1,pascal1)
        
        
        return getP(self,rowIndex,[1])
        