import itertools
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
            def sum1(c_start,r_start,index):
                s_col=sum(grid[row][index+c_start] for row in range(r_start,r_start+3))
                s_row=sum(grid[index+r_start][col] for col in range(c_start,c_start+3))
                diag1=sum(grid[row][col] for row,col in zip(range(r_start,r_start+3),range(c_start,c_start+3)))
                diag2=sum(grid[row][col] for row,col in zip(range(r_start+2,-1,-1),range(c_start,c_start+3)))
            
                return [s_col,s_row,diag1,diag2]
            
            def Not_unique(r_start,c_start):
                square={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
                
                for row in range(r_start,r_start+3):
                    
                    for col in range(c_start,c_start+3):
                        
                        if grid[row][col] in square:
                            
                        
                            if square[grid[row][col]]==1:
                            
                                return True
                            else:
                                square[grid[row][col]]+=1
                        else:
                            return True
                return False
                  
            row=len(grid)
            col=len(grid[0])
            magic_s=0
            r_start=0
            c_start=0
        
            while r_start<row-2:
                
                c_start=0
                
                while c_start<len(grid[0])-2:
                    
                    magic_s+=1
                    orgin_s=sum1(c_start,r_start,0)
                    uni=Not_unique(r_start,c_start)
                    
                    for index in range(3):
                        
                        sums=sum1(c_start,r_start,index)
                                 
                        if   sums[2]!=sums[3] or orgin_s[1]!=sums[1] or orgin_s[0]!=sums[0] or  uni:
                            
                            magic_s-=1
                            break
                    
                    c_start+=1
                    
                r_start+=1
                    
            return magic_s
                
                    
            
                    
                    
                    
                    
                    
                
                    
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         row=3
#         col=3
#         r_start=0
#         c_start=0
#         magic=0
#         column=0
#         rows=0
#         next_box=True
        
#         if len(grid)<3 or len(grid)<3:
#             return magic
        
#         while r_start<len(grid)-2:
         
            
#             while c_start<len(grid[0])-2:
#                 next_box=True
#                 same_col=0
#                 same_row=0
#                 diag1=0
#                 diag2=0
                
                
#                 for r in range(r_start,row):
#                     column=0
#                     pre_col=0
            
#                     for c in range(c_start,col):
                
#                         column+=grid[r][c]
#                         if grid[r][c]>9 or  grid[r][c]<1:
#                              next_box=False
                    
#                         if pre_col!=grid[r][c]:
#                              pre_col=column
#                         else:
                           
#                             next_box=False
                        
#                         if r-r_start==c-c_start:   
#                             diag1+=grid[r][c]
                    
#                         if r+c==col-1:
                            
#                             diag2+=grid[r][c]
                            
#                     if same_col==0 :
#                         same_col=column
#                     elif column!=same_col:
#                         print("hll")
#                         next_box=False
#                         break   
                        
                    
#                 for c in range(c_start,col):
#                     rows=0
#                     for r in range(r_start,row):
                    
#                         rows+=grid[r][c]
                            
#                     if  same_row==0:
#                         # print("hll")
#                         same_row=rows
#                     elif rows!=same_row:
#                         # print("hll")
#                         next_box=False
#                         break   
                    
                
#                 if diag1!=same_col or  diag1!=diag2:
#                     next_box=False
#                 if next_box:
#                     magic+=1
                    
#                 c_start+=1
#                 col+=1
                
#             c_start=0
#             col=3
#             r_start+=1
#             row+=1
#         return magic
            
#                 [[3,2,9,2,7],
#                  [6,1,8,4,2],
#                  [7,5,3,2,7],
#                  [2,9,4,9,6],
#                  [4,3,8,2,5]]