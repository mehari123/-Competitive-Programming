def squares():
    squares=[]
    square1=list(map(int,input().split()))
    square2=list(map(int,input().split()))
    squares.append(square1)
    squares.append(square2)
    return squares
    
    
def is_square():
    
    square=squares()
    
    s1_s=0
    s2_s=2
    loop1=1
    loop2=1
    
    while s1_s<2:
      
        s2_s=0
        while s2_s<2:
        
            if square[0][s1_s]==square[1][s2_s]:
            
                if (square[0][loop1] + square[1][loop2])==square[0][s1_s]:
                    return "YES"
            loop2-=1
            s2_s+=1
        loop1-=1
        s1_s+=1
    return "NO"

test_case=int(input())

for test in range(test_case):
    
    print(is_square())
    
        
