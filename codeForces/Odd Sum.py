n=int(input())
 
arr=list(map(int,input().split()))
 
arrange=False
pointer1=0
pointer2=n
sum1=sum(arr[:pointer2])
sum2=sum(arr[pointer2:])
if sum1!=sum2:
    arrange=True
else:
    while pointer1<n:
        pointer2=n
        while pointer2<(2*n):
            if arr[pointer1]<arr[pointer2] or arr[pointer1]>arr[pointer2]:
        
                arr[pointer1],arr[pointer2]=arr[pointer2],arr[pointer1]
                arrange=True
                break
            pointer2+=1
        if arrange:
            break
        pointer1+=1
    
if arrange:
    print(' '.join(map(str,arr)))
else:
    print(-1)
