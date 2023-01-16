class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ball_box=[]
        ans=[]

        for index,box in enumerate(boxes):
            if box=="1":
                ball_box.append(index)
        
        size=len(boxes)
        index=0
        ans=[]
        while index<size:
            operation=0
            for ball in ball_box:
                operation+=abs(ball-index)
            
            ans.append(operation)
            index+=1
        return ans
            
            

                
    