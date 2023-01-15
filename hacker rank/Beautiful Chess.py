def attac_place():
    empty=input()
    attacked=[]
    for index in range(8):
        
        line=list(map(str,input().split()))
        line=list(line[0])
        if len(attacked)<2:
            attacked=[]
        for index2,line in enumerate(line):
            
                
            if line=="#" and len(attacked)<2:
                attacked.append([index,index2])
    return attacked
                
def ans():
        attacked=attac_place()
        row1=attacked[0][0]
        col1=attacked[0][1]
        row2,col2=attacked[1][0],attacked[1][1]
        le_mat=8
        while le_mat>0:
        
            if row1==row2 and col1==col2:
                return str(row1+1)+" "+str(col1+1)
            row1+=1
            col1+=1
            row2+=1
            col2-=1
            le_mat-=1
                

test_case=int(input())

while test_case>0:
    print(ans())
    test_case-=1
