num = int(input())

count = 0

while num > 0:
    
    d = 1
    while 2 ** d <= num:
        
        d += 1
        
    d = d-1
    num = (num - (2 ** d ))
    count +=1
 
print(count)   
