test=int(input())

for i in range(test):
    n,k=map(int,input().split())
    array=list(map(int,input().split()))
    
    set1=set()
    
    for num in array:
        set1.add(num)
    prin="NO"  
    for num in array:
        if num+k in set1:
            prin="YES"
            break
    print(prin)
