test=int(input())
 
for i in range(test):
    n=int(input())
    array=list(map(int,input().split()))
 
    ans="YES"
    index=0
    array.sort()
    while index<len(array)-1:
        if abs(array[index]-array[index+1])>1:
            ans="NO"
            break
        index+=1
    print(ans)
