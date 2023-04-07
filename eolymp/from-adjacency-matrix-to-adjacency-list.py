size = int(input())
adjecency = {i:set() for i in range(1,size + 1)}

for row in range(1,size + 1):
    
    row_ls = input().strip().split()
    
    for index,c in enumerate(row_ls):
       
        if c == "1":
            
            adjecency[row].add(index + 1)
            

for key,value in adjecency.items():
    
    if len(value) == 0:
        print("")
    else:
        print(len(value)," ".join([str(i) for i in value]))