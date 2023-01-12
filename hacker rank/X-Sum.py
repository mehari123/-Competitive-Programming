from collections import defaultdict
def matrix():
    
    row,col=map(int,input().split())
    
    mat=[]
    
    index=0
    
    while index <row:
        x = input().split()
        mat.append(list(map(int, x)))
        index+=1
    return mat

test_case=int(input())



for test in range(test_case):
    
    matrix1=matrix()
    right_diag=defaultdict(int)
    left_diag=defaultdict(int)
    
    for row in range(len(matrix1)):
        
        for col in range(len(matrix1[0])):
            
            right=row-col
            left=row+col
            
            right_diag[right]+=matrix1[row][col]
            left_diag[left]+=matrix1[row][col]
    
    max_attack=0
    
    for row in range(len(matrix1)):
        
        for col in range(len(matrix1[0])):
            
            if right_diag[row-col]+left_diag[row+col]-matrix1[row][col]>max_attack:
                
                max_attack=right_diag[row-col]+left_diag[row+col]-matrix1[row][col]
    
    print(max_attack)
               
