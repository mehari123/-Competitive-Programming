class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        self.visited = set()
        self.color1 = image[sr][sc]
        def fldfill(i,j):
            
            directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            self.visited.add(str(i) + str(j))
            image[i][j] = color
            
            for di in directions:
                
                if di[0] >= 0 and di[1] >= 0  and di[0] < len(image) and di[1] <len(image[0]) and(image[di[0]][di[1]] == self.color1) and ((str(di[0]) + str(di[1])) not in self.visited):
                    
                    fldfill(di[0],di[1])
                    
       
        fldfill(sr,sc)
        return image
                    
                    
        