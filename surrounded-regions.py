class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board = board
        col = len(board[0])
        row = len(board)
        visited = set()
        def dfs(i,j):
            nonlocal board
            if i <0 or i >= len(board) or j < 0 or j >= len(board[0]) :
                
                 return
            
            if 0 <= i <= len(board) and 0 <= j <= len(board[0]) and tuple([i,j]) not in visited and board[i][j] == "O":
                
                visited.add(tuple([i,j]))
                board[i][j] = "1"
                directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
                
                for di in directions:
                    
                    dfs(di[0],di[1])
                     
        for j in range(len(board[0])):
            
            dfs(0,j)
            dfs(row-1,j)
            
        
        for i in range(len(board)):
            
            dfs(i,0)
            dfs(i,col-1)
            
        
        for i in range(len(board)):
            
            for j in range(len(board[0])):
                
                if board[i][j] == "O":
                    
                    board[i][j]= "X"
                    
                elif board[i][j] == "1":
                    
                    board[i][j] = "O"
                    
        return board
        
            
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             def is_region(i,j):
            
#             nonlocal tup
#             directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
#             visited.add(tuple([i,j]))
#             tup.add(tuple([i,j]))
            
#             for di in directions:
                
#                 if 0 > di[0] or di[0] >= len(board) or 0 > di[1] or di[1] >= len(board[0]):
                    
#                     tup = set()
#                     return tup
#                     break
#                 elif board[di[0]][di[1]] == "O" and tuple([di[0],di[1]]) not in visited:
                    
#                     is_region(di[0],di[1])
                    
#                 visited.add(tuple([di[0],di[1]]))
                
#             return tup 
                        
#         for i in range(len(board)):
            
#             for j in range(len(board[0])):
                
#                 if tuple([i,j]) not in visited and board[i][j] != "X" and (i != len(board)-1) and j != len(board[0])-1 and i != 0 and j != 0:
                    
#                     tup = set()
#                     is_region(i,j)
#                     tup = tuple(tup)
#                     if tup:
                        
#                         for t in tup:
                            
#                             region.add(t)
                
#                 if board[i][j] == "X":
                    
#                     visited.add(tuple([i,j]))
                    
    
#         for re in region:
            
#             r = tuple(re)
            
#             board[r[0]][r[1]] = "X"