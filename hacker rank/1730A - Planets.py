test_case=int(input())

for test in range(test_case):
    
    num_p_c=list(map(int,input().split()))
    
    orbits=list(map(int,input().split()))
    
    oribit_count={}
    
    for orbit in orbits:
        
        if orbit in oribit_count:
            oribit_count[orbit]+=1
        else:
            oribit_count[orbit]=1
    
    cost=0
    for key, value in oribit_count.items():
        
        if value==1:
            cost+=1
        else:
            cost+=min(value,num_p_c[1])
            
    print(cost)
